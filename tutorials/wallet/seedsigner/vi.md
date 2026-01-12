---
name: SeedSigner
description: Phần cứng wallet tự làm, không trạng thái, giá cả phải chăng và hoàn toàn không có khoảng cách không khí
---

![cover](assets/cover.webp)



SeedSigner là phần cứng wallet Bitcoin mã nguồn mở mà bất kỳ ai cũng có thể tự chế tạo bằng các linh kiện điện tử đa năng giá rẻ. Không giống như các sản phẩm thương mại như Ledger, Coldcard hay Trezor, đây không phải là một thiết bị sẵn sàng sử dụng do một công ty sản xuất: đây là một dự án cộng đồng cho phép bất kỳ ai cũng có thể tự tạo thiết bị của riêng mình và kiểm soát mọi bước.



SeedSigner được thiết kế để hoạt động 100% ***không kết nối mạng***: nó không bao giờ kết nối Internet, không có Wi-Fi hoặc Bluetooth (trong trường hợp của Raspberry Pi Zero v1.3) và không bao giờ được kết nối với máy tính để trao đổi dữ liệu. Giao tiếp chỉ được thực hiện thông qua hệ thống trao đổi mã QR. Cụ thể, phần mềm quản lý danh mục đầu tư của bạn (chẳng hạn như Sparrow Wallet) sẽ hiển thị giao dịch cần ký dưới dạng mã QR; bạn quét chúng bằng camera của SeedSigner, sau đó thiết bị sẽ ký giao dịch bằng khóa riêng tư được lưu trữ tạm thời trong RAM. Cuối cùng, nó tạo mã QR chứa giao dịch đã ký, bạn quét mã QR này bằng phần mềm của mình để gửi đến mạng Bitcoin.



![Image](assets/fr/001.webp)



SeedSigner cũng ***không lưu trữ trạng thái***. Nói cách khác, nó không lưu trữ seed hoặc khóa riêng tư của bạn vĩnh viễn, không giống như các ví phần cứng khác. Mỗi khi bạn khởi động lại, bộ nhớ của nó sẽ hoàn toàn trống, trừ khi bạn cấu hình thiết bị để lưu cài đặt trên thẻ nhớ microSD. Do đó, bạn phải nhập lại seed mỗi khi sử dụng, phương pháp thiết thực nhất là lưu trữ nó dưới dạng mã QR, để quét khi khởi động bằng camera của SeedSigner. Chế độ hoạt động này làm giảm đáng kể bề mặt bị tấn công: ngay cả khi kẻ trộm đánh cắp thiết bị của bạn, hắn sẽ không tìm thấy bất kỳ thông tin nào trên đó, vì nó luôn trống theo mặc định.



Một lựa chọn khác để lưu trữ seed và sử dụng nó với SeedSigner là sử dụng thẻ thông minh *SeedKeeper* kết hợp với đầu đọc tương thích. Điều này cung cấp cho bạn một *Phần tử Bảo mật* rất mạnh mẽ để lưu trữ seed, đồng thời sử dụng màn hình SeedSigner để ký giao dịch. Tuy nhiên, cấu hình cụ thể này sẽ được trình bày trong một hướng dẫn chuyên sâu khác. Ở đây, chúng ta sẽ tập trung vào cách sử dụng SeedSigner cơ bản:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Dự án SeedSigner chiếm một vị trí quan trọng trong hệ sinh thái Bitcoin, vì nó mang đến cho mọi người, ở mọi nơi trên thế giới, cơ hội được hưởng lợi từ hệ thống bảo mật tiên tiến để bảo vệ bitcoin của họ. Ưu điểm chính của nó nằm ở khả năng tiếp cận: phần cứng cần thiết có thể được mua với giá dưới 50 đô la. Hơn nữa, nó cho phép người dân sống ở các quốc gia bị hạn chế tự xây dựng phần cứng wallet của riêng họ từ các linh kiện máy tính tiêu chuẩn, dễ tìm và ít bị ràng buộc bởi các quy định.



Nhưng ngay cả bên ngoài những bối cảnh cụ thể này, SeedSigner vẫn có thể là một lựa chọn thú vị dành cho bạn: mã nguồn mở, hoạt động không trạng thái và không có khoảng cách, đồng thời giảm các hướng tấn công liên quan đến chuỗi cung ứng phần cứng wallet của bạn.



## 1. Thiết bị cần thiết



Để xây dựng SeedSigner, bạn sẽ cần các thành phần sau:





- Raspberry Pi Zero
    - Phiên bản 1.3 được khuyến nghị vì không có Wi-Fi hoặc Bluetooth, đảm bảo khả năng cách ly hoàn toàn.
 - Phiên bản W và v2 cũng tương thích, nhưng tích hợp chip Wi-Fi/Bluetooth. Do đó, bạn nên vô hiệu hóa nó bằng cách tháo module radio ra khỏi card. Thao tác này tương đối đơn giản, nhưng đòi hỏi sự chính xác (kìm nhỏ là đủ cho Zero W, trong khi v2 cần bút nóng để tháo tấm kim loại che module). Tôi sẽ không đi sâu vào chi tiết trong hướng dẫn này, nhưng bạn sẽ tìm thấy tất cả hướng dẫn trong tài liệu này: *[Vô hiệu hóa WiFi/Bluetooth bằng phần cứng](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Xin lưu ý: một số mẫu Raspberry Pi Zero được bán mà không có chân GPIO hàn sẵn. Bạn có thể mua phiên bản có chân tích hợp trực tiếp (giải pháp đơn giản nhất) hoặc mua riêng chân và tự hàn (giải pháp phức tạp hơn).
 - Đừng quên cung cấp nguồn điện micro-USB.



![Image](assets/fr/002.webp)





- Màn hình Waveshare 1,3" (240×240 px)** (bằng tiếng Pháp)
    - Điều quan trọng là phải chọn đúng mẫu máy này: có nhiều màn hình tương tự khác, nhưng độ phân giải khác nhau. Nếu không có độ phân giải 240x240 px, màn hình sẽ không sử dụng được.
    - Màn hình có ba nút bấm và một cần điều khiển nhỏ để điều khiển giao diện người dùng.



![Image](assets/fr/003.webp)





- Camera tương thích với Raspberry Pi Zero**
    - Lựa chọn 1: máy ảnh tiêu chuẩn có tấm lót vàng rộng (kiểm tra khả năng tương thích với vỏ máy của bạn).
    - Lựa chọn 2: camera "*Zero*" nhỏ gọn hơn, được thiết kế riêng cho Pi Zero.



![Image](assets/fr/004.webp)





- Thẻ nhớ MicroSD**
    - Dung lượng khuyến nghị: từ 4 đến 32 GB.





- Nhà ở (tùy chọn nhưng được khuyến nghị)** (tùy chọn nhưng được khuyến nghị)** (tùy chọn nhưng được khuyến nghị)** (tùy chọn nhưng được khuyến nghị)**)
    - Bảo vệ thiết bị và giúp sử dụng dễ dàng.
    - Mô hình phổ biến nhất là "*Hộp thuốc màu cam*", trong đó [có sẵn các tệp STL nguồn mở để in 3D](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Hộp cũng có sẵn từ [các nhà bán lẻ độc lập có liên kết với dự án](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Bạn có thể mua riêng lẻ các thành phần này hoặc, để đơn giản hơn, hãy chọn gói sản phẩm đóng gói sẵn bao gồm tất cả phần cứng cần thiết. Cá nhân tôi đã đặt mua gói sản phẩm của mình [trên trang web tiếng Pháp này](https://bitcoinbazar.fr/), nhưng bạn cũng có thể tìm thấy danh sách các nhà cung cấp cho từng khu vực trên thế giới trên [trang phần cứng của dự án SeedSigner](https://seedsigner.com/hardware/). Nếu bạn muốn mua riêng lẻ các thành phần, chúng có sẵn trên các nền tảng thương mại điện tử lớn hoặc tại các cửa hàng chuyên dụng.



## 2. Chuẩn bị phần mềm



Sau khi chuẩn bị xong phần cứng, bạn cần chuẩn bị thẻ nhớ microSD bằng cách cài đặt hệ thống SeedSigner. Để thực hiện, hãy vào máy tính cá nhân thường dùng của bạn và cắm thẻ nhớ microSD dành cho SeedSigner vào.



### 2.1. Tải xuống



Truy cập [kho lưu trữ GitHub chính thức của dự án](https://github.com/SeedSigner/seedsigner/releases). Trên phiên bản phần mềm mới nhất, hãy tải xuống:




- Hình ảnh `.img` tương ứng với mô hình Pi của bạn.
- Tệp `.sha256.txt`.
- Tệp `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Trước khi bắt đầu cài đặt, hãy kiểm tra phần mềm.



### 2.2 Xác minh trên Linux và macOS



Bắt đầu bằng cách nhập khóa công khai chính thức của dự án SeedSigner trực tiếp từ Keybase:



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal sẽ thông báo cho bạn biết khóa đã được nhập hoặc cập nhật. Tiếp theo, hãy chạy lệnh xác minh trên tệp chữ ký (nhớ sửa đổi lệnh theo phiên bản của bạn, ở đây là `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Nếu mọi thứ đều chính xác, đầu ra sẽ hiển thị `Good signature`. Điều này có nghĩa là tệp `.sha256.txt` đã được ký bằng khóa bạn vừa nhập và chữ ký đó hợp lệ. Bỏ qua thông báo cảnh báo `WARNING: This key is not certified with a trusted signature`: điều này là bình thường, vì giờ đây bạn cần kiểm tra xem khóa được sử dụng có thuộc về dự án SeedSigner hay không.



Để thực hiện việc này, hãy so sánh 16 ký tự cuối cùng của dấu vân tay được hiển thị với các ký tự có sẵn trên [Keybase.io/SeedSigner](https://keybase.io/seedsigner), trên [Twitter chính thức](https://twitter.com/SeedSigner/status/1530555252373704707) hoặc trong tệp được công bố trên [SeedSigner.com](https://seedsigner.com/keybase.txt). Nếu các mã định danh này khớp chính xác, bạn có thể chắc chắn rằng khóa đó thực sự là của dự án. Nếu nghi ngờ, hãy dừng lại ngay lập tức và yêu cầu cộng đồng SeedSigner (Telegram, X, GitHub...) hỗ trợ.



Khi khóa đã được xác thực, bạn có thể kiểm tra xem hình ảnh đã tải xuống có bị sửa đổi không (nhớ sửa đổi lệnh theo phiên bản của bạn, ở đây là `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Trên Linux, lệnh này được tích hợp sẵn.
- Cảnh báo: Các phiên bản macOS trước `Big Sur (11)` không nhận ra tùy chọn `--ignore-missing`. Trong trường hợp này, hãy xóa tùy chọn này và bỏ qua các cảnh báo về tệp bị thiếu.



Kết quả mong đợi là `OK` bên cạnh tệp `.img`. Điều này xác nhận rằng hình ảnh được tải lên giống hệt với hình ảnh do dự án xuất bản và chưa bị chỉnh sửa.



### 2.3 Xác minh Windows



Trên Windows, quy trình tương tự nhưng các lệnh thì khác. Bắt đầu bằng cách cài đặt [Gpg4win](https://www.gpg4win.org/) và mở ứng dụng *Kleopatra*. Nhập khóa công khai của dự án SeedSigner từ URL Keybase:



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Tiếp theo, hãy mở PowerShell trong thư mục chứa các tệp đã tải xuống (`Shift` + nhấp chuột phải > `Mở PowerShell tại đây`). Chạy lệnh sau để kiểm tra chữ ký manifest (nhớ sửa đổi lệnh theo phiên bản của bạn, ở đây là `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Nếu mọi thứ đều chính xác, đầu ra sẽ hiển thị `Good signature`. Điều này có nghĩa là tệp `.sha256.txt` đã được ký bằng khóa bạn vừa nhập và chữ ký đó hợp lệ. Bỏ qua thông báo cảnh báo `WARNING: This key is not certified with a trusted signature`: điều này là bình thường, vì giờ đây bạn cần kiểm tra xem khóa được sử dụng có thuộc về dự án SeedSigner hay không.



Để thực hiện việc này, hãy so sánh 16 ký tự cuối cùng của dấu vân tay được hiển thị với các ký tự có sẵn trên [Keybase.io/SeedSigner](https://keybase.io/seedsigner), trên [Twitter chính thức](https://twitter.com/SeedSigner/status/1530555252373704707) hoặc trong tệp được công bố trên [SeedSigner.com](https://seedsigner.com/keybase.txt). Nếu các mã định danh này khớp chính xác, bạn có thể chắc chắn rằng khóa đó thực sự là của dự án. Nếu nghi ngờ, hãy dừng lại ngay lập tức và yêu cầu cộng đồng SeedSigner (Telegram, X, GitHub...) hỗ trợ.



Sau khi khóa đã được xác thực, bạn cần kiểm tra xem tệp hình ảnh có bị hỏng không. Để thực hiện việc này, hãy sử dụng lệnh sau trong PowerShell:



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Ví dụ cho Raspberry Pi Zero 2 (nhớ sửa đổi lệnh theo phiên bản của bạn, ở đây là `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



Sau đó, PowerShell sẽ tính toán hàm băm SHA256 của tệp hình ảnh. So sánh hàm băm này với giá trị tương ứng trong `seedsigner.0.8.6.sha256.txt`.




- Nếu hai giá trị hoàn toàn giống hệt nhau thì quá trình kiểm tra đã thành công và bạn có thể tiếp tục.
- Nếu chúng khác nhau, tức là tệp đã bị hỏng hoặc lỗi. Đừng sử dụng và hãy bắt đầu tải xuống lại.



![Image](assets/fr/013.webp)



Việc xác minh thành công đảm bảo rằng tệp `.img` của bạn vừa xác thực (được SeedSigner ký) vừa không bị thay đổi (chưa chỉnh sửa). Sau đó, bạn có thể yên tâm chuyển sang bước tiếp theo.



### 2.4. Flash hình ảnh



Nếu bạn chưa có, hãy tải xuống phần mềm [Balena Etcher](https://etcher.balena.io/), sau đó:




- Cắm thẻ nhớ microSD vào máy tính.
- Khởi chạy Etcher.
- Chọn tệp `.img` đã tải xuống và xác minh.
- Chọn thẻ nhớ microSD làm mục tiêu.
- Nhấp vào `Flash!`.



![Image](assets/fr/014.webp)



Chờ cho đến khi quá trình hoàn tất: thẻ nhớ microSD của bạn đã sẵn sàng để sử dụng. Giờ là lúc lắp ráp!



## 3. Lắp ráp SeedSigner



Sau khi thẻ nhớ microSD của bạn đã được chuẩn bị và flash bằng phần mềm SeedSigner, bạn có thể tiến hành lắp ráp hoàn thiện. Hãy dành thời gian, vì một số bộ phận khá dễ vỡ (đặc biệt là khăn trải bàn, camera và chân GPIO).



### 3.1 Chuẩn bị nhà ở



Trước tiên, hãy mở hộp đựng. Kiểm tra xem hộp có sạch sẽ không và không có nhựa in 3D nào còn sót lại trên các chốt bên trong. Hãy chú ý:




- Vị trí camera (lỗ tròn nhỏ ở phía trước).
- Mở màn hình.
- Các lỗ cắt cho cổng micro-USB và khe cắm thẻ nhớ microSD của Raspberry Pi Zero.



### 3.2 Lắp đặt camera



Xác định vị trí đầu nối ribbon camera trên Raspberry Pi Zero: đó là một dải đen mỏng ở cạnh bo mạch, có thể nhấc nhẹ lên để mở. Hãy nhấc nó lên một cách cẩn thận, không dùng lực: nó chỉ cần nghiêng một vài mm.



![Image](assets/fr/015.webp)



Lắp nắp camera. Phần màu nâu/đồng phải hướng xuống dưới. Đảm bảo nắp được lắp chặt vào đầu nối, không bị xoắn.



![Image](assets/fr/016.webp)



Đóng thanh đen để khóa khăn trải bàn (bạn sẽ cảm thấy tiếng tách nhẹ). Nhẹ nhàng kiểm tra xem khăn có cố định tại chỗ và không bị xê dịch không.



![Image](assets/fr/017.webp)



Sau đó, đặt mô-đun camera vào lỗ thích hợp trên vỏ. Tùy thuộc vào kiểu máy, camera có thể được gắn trực tiếp hoặc cần một dải keo nhỏ để giữ cố định. Ống kính phải được căn chỉnh hoàn hảo, hướng ra ngoài.



### 3.3 Cài đặt Raspberry Pi Zero



Nếu bạn sử dụng vỏ case, hãy lắp bo mạch Raspberry Pi Zero vào bên trong. Cẩn thận căn chỉnh các cổng với các lỗ mở có sẵn.



Sau đó, đặt màn hình Waveshare lên trên Raspberry Pi Zero. Các chân GPIO của Pi phải thẳng hàng với đầu nối cái của màn hình. Nhẹ nhàng ấn màn hình vào các chân, ấn đều cả hai bên để tránh làm cong màn hình.



![Image](assets/fr/018.webp)



Nếu bạn có vỏ máy, hãy hoàn thiện việc lắp ráp bằng cách thêm mặt trước và cần điều khiển.



Cuối cùng, lắp thẻ nhớ microSD chứa phần mềm đã cài đặt vào khe cắm gắn cạnh của Raspberry Pi Zero. Đảm bảo thẻ khớp vào đúng vị trí.



### 3.4 Khởi động lần đầu



Cắm cáp nguồn micro-USB vào cổng chuyên dụng. Chờ khoảng một phút. Logo SeedSigner sẽ xuất hiện, sau đó là màn hình chính.



![Image](assets/fr/019.webp)



Trước tiên, hãy kiểm tra xem các thành phần khác nhau có hoạt động bình thường không bằng cách vào menu `Cài đặt > Kiểm tra I/O`.



![Image](assets/fr/020.webp)



Kiểm tra tất cả các nút và đảm bảo chúng phản hồi chính xác. Sau đó, nhấp vào nút `KEY1` để kiểm tra xem camera có hoạt động bình thường không. Thao tác này sẽ chụp ảnh.



![Image](assets/fr/021.webp)



### 3.5 Điều chỉnh máy ảnh



Tùy thuộc vào cách bạn lắp đặt SeedSigner, camera có thể hiển thị hình ảnh bị đảo ngược. Để khắc phục điều này, hãy vào `Cài đặt > Nâng cao > Xoay camera` và chọn xoay 180° nếu cần.



![Image](assets/fr/022.webp)



Nếu bạn đã thay đổi hướng camera hoặc muốn thay đổi các cài đặt khác (chẳng hạn như ngôn ngữ giao diện) sau này, bạn sẽ cần bật tính năng lưu trữ cài đặt trên thẻ nhớ microSD. Nếu không, cài đặt của bạn sẽ trở về mặc định mỗi khi bạn khởi động lại, vì Raspberry Pi Zero không có bộ nhớ lưu trữ.



Để thực hiện việc này, hãy mở menu `Cài đặt > Cài đặt cố định`, sau đó chọn `Đã bật`.



![Image](assets/fr/023.webp)



Nếu mọi thứ đều hoạt động bình thường, SeedSigner của bạn đã sẵn sàng để sử dụng!



## 4. Cài đặt SeedSigner



Trước khi tạo Bitcoin wallet, hãy cấu hình SeedSigner. Vì SeedSigner chạy trên Raspberry Pi Zero không có bộ nhớ liên tục, nên các thiết lập của nó sẽ không được tự động lưu trừ khi bạn lưu chúng vào thẻ nhớ microSD. Vì vậy, hãy đảm bảo bạn đã bật tùy chọn này, nếu không các thiết lập này sẽ bị mất khi khởi động lại (xem bước 3.5).



### 4.1 Truy cập menu tham số



Khởi động SeedSigner và chờ màn hình chính xuất hiện. Sử dụng cần điều khiển, điều hướng đến tùy chọn `Cài đặt`, sau đó xác thực bằng cách nhấn nút giữa. Bây giờ bạn sẽ vào menu cài đặt chính.



![Image](assets/fr/024.webp)



### 4.2 Lựa chọn phần mềm quản lý danh mục đầu tư



Sau đó truy cập vào menu `Phần mềm điều phối`.



![Image](assets/fr/025.webp)



`Coordinator` là phần mềm quản lý danh mục đầu tư mà SeedSigner của bạn sẽ giao tiếp thông qua mã QR. Phần mềm này được cài đặt trên máy tính hoặc điện thoại thông minh của bạn. Nó sẽ cho phép bạn quản lý bitcoin của mình mà không cần truy cập vào khóa riêng tư. SeedSigner vẫn là thiết bị duy nhất có khả năng ký các giao dịch của bạn.



Phiên bản firmware hiện tại hỗ trợ một số chương trình: Sparrow, Spectre, BlueWallet, Nunchuk và Keeper. Trong trường hợp của tôi, tôi sử dụng **Sparrow Wallet**, tôi đặc biệt khuyên dùng vì tính đơn giản và nhiều chức năng.



Nếu bạn không biết cách cài đặt, bạn có thể làm theo hướng dẫn này:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Chỉ cần chọn phần mềm bạn muốn từ menu.



![Image](assets/fr/026.webp)



### 4.3 Hiển thị đơn vị và số tiền



Trong menu `Hiển thị mệnh giá`, bạn có thể chọn đơn vị để hiển thị số tiền:




- `BTC`
- mBTC` (milli-bitcoin, hoặc 0,001 BTC)
- gW-15 (satoshi, hoặc 1/100.000.000 BTC)



Thiết bị **sats** thường là thiết bị thiết thực nhất cho số lượng nhỏ.



![Image](assets/fr/027.webp)



### 4.4 Cài đặt nâng cao



Bây giờ hãy vào menu `Nâng cao`. Tại đây bạn sẽ tìm thấy một số tùy chọn hữu ích:




- Mạng gW-17`: chỉ được sửa đổi nếu bạn muốn sử dụng SeedSigner trên Testnet.
- Mật độ mã QR: điều chỉnh lượng thông tin chứa trong mỗi mã QR. Bạn có thể giữ nguyên giá trị mặc định, trừ khi bạn thấy khó đọc khi quét.
- `Xpub export`: bật hoặc tắt tính năng xuất khóa công khai mở rộng (`xpub`, `ypub`, `zpub`) sang phần mềm quản lý danh mục đầu tư thông qua mã QR (một chức năng chúng ta sẽ sử dụng sau, vì vậy hãy để nó được bật ngay bây giờ).
- `Script types`: định nghĩa các loại script được phép khóa bitcoin của bạn. Bạn không cần phải sửa đổi tham số này, vì loại script sẽ được đặt trực tiếp thành Sparrow. Ở đây, chỉ những script mà SeedSigner được phép thao tác mới được quan tâm.



### 4.5 Lựa chọn ngôn ngữ



Cuối cùng, trong menu `Ngôn ngữ`, bạn có thể thay đổi ngôn ngữ giao diện cho phù hợp với sở thích của mình.



![Image](assets/fr/028.webp)



## 5. Tạo và lưu seed



seed (hay còn gọi là cụm từ ghi nhớ) là nền tảng cho danh mục đầu tư Bitcoin của bạn. Nó được sử dụng để lấy khóa riêng và địa chỉ, đồng thời cung cấp quyền truy cập vào quỹ của bạn. SeedSigner cung cấp một số phương pháp để tạo ra nó, chúng ta sẽ xem xét trong phần này.



Trước khi bắt đầu, chúng ta có một số lời nhắc nhở quan trọng:




- Cụm từ này cung cấp quyền truy cập đầy đủ, không hạn chế vào tất cả bitcoin của bạn.** Bất kỳ ai sở hữu cụm từ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập trực tiếp vào SeedSigner của bạn;
- Thông thường, một cụm từ 12 từ được sử dụng để khôi phục wallet trong trường hợp phần cứng wallet bị mất hoặc bị đánh cắp. Tuy nhiên, vì SeedSigner là một thiết bị *không trạng thái*, nó không bao giờ đăng ký seed của bạn. Vì vậy, các bản sao lưu vật lý của bạn không chỉ đơn thuần là bản sao lưu, mà là **cách duy nhất để sử dụng wallet**. Nếu bạn làm mất những bản sao lưu này, bitcoin của bạn sẽ bị mất vĩnh viễn. Vì vậy, hãy sao lưu chúng cẩn thận, trên nhiều phương tiện lưu trữ và ở những nơi an toàn;
- Nếu bạn mới bắt đầu, tôi thực sự khuyên bạn nên đọc hướng dẫn này để hiểu rõ hơn về những rủi ro liên quan đến việc quản lý cụm từ ghi nhớ:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Truy cập công cụ tạo seed



Từ màn hình chính của SeedSigner, hãy vào menu `Công cụ`.



![Image](assets/fr/029.webp)



Bây giờ bạn sẽ tạo mã generate cho seed. seed đơn giản là một số ngẫu nhiên lớn. Số này được tạo ra càng ngẫu nhiên thì càng an toàn. SeedSigner cung cấp hai cách để thực hiện việc này:




- "camera": seed được tạo ra từ nhiễu hình ảnh của một bức ảnh. Bạn chụp một bức ảnh của một môi trường ngẫu nhiên (vật thể, phong cảnh, khuôn mặt, v.v.) với các biến thể pixel được sử dụng để tính toán entropy generate. Đây là một phương pháp nhanh, nhưng không thể tái tạo.
- "Dice Roll": bạn tung xúc xắc để tạo ra entropy cần thiết. Phương pháp này tốn thời gian hơn, nhưng có thể tái tạo và do đó có thể kiểm chứng được. Nếu bạn chọn phương pháp này, hãy làm theo lời khuyên trong hướng dẫn này (không cần tính toán tổng kiểm tra ở đây, SeedSigner sẽ lo việc đó):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Tạo seed bằng ảnh



Nếu bạn chọn phương pháp chụp ảnh, hãy nhấp vào `New seed` (có biểu tượng máy ảnh), chụp ảnh và xác thực. Sau đó, chọn độ dài câu (12 hoặc 24 từ), độ dài này sẽ hiển thị trên màn hình để lưu. Các bước sau đây giống hệt với phần 5.3.



### 5.3 Tạo seed bằng xúc xắc



Trong hướng dẫn này, chúng ta sử dụng phương pháp **Lăn Xúc Xắc**. Nhấp vào `New seed` (có biểu tượng xúc xắc).



![Image](assets/fr/030.webp)



Sau đó chọn độ dài của cụm từ ghi nhớ. 12 từ đã mang lại mức độ bảo mật đủ tốt, vì vậy đây là lựa chọn tôi khuyên bạn nên làm.



![Image](assets/fr/031.webp)



Lăn xúc xắc và nhập số kết quả bằng con trỏ. Nhấn nút giữa để xác nhận mỗi lần nhập. Nếu nhập sai, bạn có thể quay lại. Sử dụng nhiều xúc xắc khác nhau để giảm thiểu ảnh hưởng của bất kỳ xúc xắc nào không cân bằng. Đảm bảo bạn không bị theo dõi trong quá trình này.



![Image](assets/fr/032.webp)



Sau khi bạn nhập 50 lần ném, SeedSigner sẽ tạo ra câu cho bạn. **Hãy làm theo hướng dẫn trong bài hướng dẫn này một cách cẩn thận nếu bạn mới bắt đầu:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Hiển thị và lưu seed



Cẩn thận viết ra các từ trong cụm từ ghi nhớ của bạn trên một vật dụng hỗ trợ thích hợp (giấy hoặc kim loại).



![Image](assets/fr/033.webp)



### 5.5 Kiểm tra bản sao lưu



Để tránh bất kỳ lỗi sao lưu nào, SeedSigner sẽ yêu cầu bạn xác minh bản sao lưu của mình. Nhấp vào `Xác minh`.



![Image](assets/fr/034.webp)



Sau đó nhập từ được yêu cầu theo thứ tự của nó trong câu. Ví dụ, ở đây tôi phải chọn từ thứ ba trong câu.



![Image](assets/fr/035.webp)



Nếu bạn mắc lỗi, SeedSigner sẽ thông báo và bạn sẽ phải bắt đầu lại, nhớ ghi lại cụm từ ghi nhớ khi được cung cấp. Bước xác minh này đảm bảo bản sao lưu của bạn chính xác và đầy đủ. Sau khi xác thực, màn hình sẽ hiển thị `Sao lưu đã được xác minh`.



![Image](assets/fr/036.webp)



Để có bài kiểm tra phục hồi đầy đủ hơn, hãy làm theo hướng dẫn này:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Hiểu khái niệm "thiết bị không trạng thái"



SeedSigner là một thiết bị không có bộ nhớ vĩnh viễn. Điều này có nghĩa là seed của bạn không bao giờ được lưu trữ bên trong thiết bị (không giống như Ledger, Trezor hay Coldcard chẳng hạn). Ngay khi bạn tắt nguồn, seed sẽ biến mất hoàn toàn khỏi RAM. Khi bạn khởi động lại, SeedSigner sẽ trở về trạng thái trống: sau đó bạn sẽ phải nhập lại seed để nó có thể ký các giao dịch của bạn.



Điều này cung cấp khả năng bảo vệ thiết yếu. Không giống như các ví phần cứng khác, SeedSigner dựa trên Raspberry Pi Zero, không có lớp bảo vệ vật lý, bao gồm cả *Secure Element*. Tuy nhiên, vì không lưu trữ dữ liệu nhạy cảm, ngay cả một thiết bị bị xâm nhập vật lý cũng không thể cho phép kẻ tấn công trích xuất khóa riêng tư hoặc tiêu thụ bitcoin của bạn.



Mặt khác, kiến trúc này cũng hàm ý một trách nhiệm bổ sung: nếu không có bản sao lưu, tiền của bạn chắc chắn sẽ bị mất. Đó là lý do tại sao tôi khuyên bạn nên sử dụng **sao lưu kép**. Bạn đã có cụm từ khôi phục: đây là bản sao lưu dài hạn chính của bạn, cần được lưu giữ ở nơi an toàn. Bây giờ, chúng ta sẽ tạo một bản sao của cụm từ này dưới dạng **mã QR**.



Mỗi lần sử dụng SeedSigner, bạn sẽ quét mã QR này bằng camera của thiết bị để tạm thời tải seed vào bộ nhớ trong khi bạn ký giao dịch. Bản sao lưu thứ hai này, dành cho mục đích sử dụng hàng ngày, cũng phải được lưu giữ hết sức cẩn thận: bất kỳ ai sở hữu mã QR này đều có toàn quyền truy cập vào bitcoin của bạn.


Tôi cũng khuyên bạn nên lưu trữ mã QR và cụm từ ghi nhớ ở hai nơi riêng biệt để tránh mất mọi thứ khi xảy ra khiếu nại.



Cuối cùng, một giải pháp thay thế tiên tiến và an toàn hơn là sử dụng SeedSigner với **SeedKeeper**, lưu trữ seed trong secure element. Để tìm hiểu thêm, hãy xem hướng dẫn này:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Ghi dấu vân tay chìa khóa chính



Sau khi xác minh hoàn tất, SeedSigner sẽ hiển thị dấu vân tay của khóa chính wallet. Dấu vân tay này sẽ nhận dạng wallet của bạn và đảm bảo bạn sử dụng đúng cụm từ khôi phục trong tương lai. Nó không tiết lộ bất kỳ thông tin nào về khóa riêng của bạn, vì vậy bạn có thể lưu trữ an toàn trên phương tiện kỹ thuật số. Chỉ cần đảm bảo bạn giữ một bản sao có thể truy cập được và không bao giờ làm mất nó.



![Image](assets/fr/037.webp)



Cũng ở giai đoạn này, bạn có thể thêm **passphrase BIP39** để tăng cường bảo mật cho wallet. Tùy thuộc vào chiến lược sao lưu của bạn, lựa chọn này có thể đáng giá, nhưng cũng tiềm ẩn rủi ro: nếu bạn mất passphrase, quyền truy cập vào bitcoin của bạn sẽ bị mất vĩnh viễn.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Nếu bạn chưa quen với khái niệm passphrase, tôi mời bạn đọc hướng dẫn toàn diện sau về chủ đề này:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Lưu seed ở định dạng QR (*SeedQR*)



SeedSigner cho phép bạn chuyển đổi mã seed thành mã QR giấy, được gọi là *SeedQR*. Phương pháp này giúp bạn nạp lại mã wallet dễ dàng hơn, vì không cần phải nhập lại từng từ theo cách thủ công.



Để thực hiện việc này, bạn cần một tờ giấy trắng hoặc mã QR kim loại tương ứng với độ dài của cụm từ ghi nhớ. Nếu bạn đã mua trọn bộ SeedSigner, các mẫu thường được bao gồm. Nếu không, bạn có thể tải xuống và in (hoặc sao chép thủ công) tại đây:




- [Định dạng 12 từ](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [định dạng 24 từ](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Định dạng gọn nhẹ 12 từ](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Định dạng gọn nhẹ 24 từ](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Từ màn hình seed, chọn `Sao lưu hạt giống`.



![Image](assets/fr/039.webp)



Sau đó chọn `Xuất dưới dạng SeedQR`.



![Image](assets/fr/040.webp)



Sau đó, chọn định dạng mong muốn (bình thường hoặc nhỏ gọn) theo mẫu giấy có sẵn.



![Image](assets/fr/041.webp)



Nhấp vào `Bắt đầu` để bắt đầu tạo *SeedQR*. Sau đó, SeedSigner sẽ hiển thị một loạt lưới (A1, A2, B1, v.v.), mỗi lưới tương ứng với một phần của mã.



![Image](assets/fr/042.webp)



Cẩn thận sao chép từng chấm đen trên trang lưu của bạn, sau đó sử dụng cần điều khiển để chuyển sang khối tiếp theo. Hãy từ từ: chỉ cần một sai lệch nhỏ cũng có thể khiến mã QR không sử dụng được.



Một vài mẹo:




- Bắt đầu bằng bút chì để bạn có thể sửa bất kỳ lỗi nào, sau đó quay lại sử dụng bút đen khi bạn hoàn thành;
- Bạn chỉ cần một điểm chính giữa hình vuông, không cần phải tô kín hoàn toàn.



![Image](assets/fr/043.webp)



Sau đó nhấp vào `Xác nhận SeedQR` và quét mã QR để kiểm tra xem mã có hoạt động chính xác không.



![Image](assets/fr/044.webp)



Nếu thông báo `Thành công` được hiển thị, *SeedQR* của bạn hợp lệ: bạn có thể tiến hành bước tiếp theo.



![Image](assets/fr/045.webp)



**Giữ tờ giấy này cẩn thận như cụm từ khôi phục của bạn. Bất kỳ ai sở hữu mã QR này đều có thể khôi phục khóa riêng tư và đánh cắp bitcoin của bạn.**



Xin chúc mừng, danh mục Bitcoin của bạn hiện đã được thiết lập và chạy! Bây giờ, chúng tôi sẽ nhập các thành phần công khai của danh mục này vào **Sparrow Wallet** để quản lý dễ dàng.



## 6. Nhập wallet vào Sparrow



Sau khi SeedSigner của bạn đã được thiết lập và seed của bạn được tạo và lưu chính xác, bước tiếp theo là liên kết danh mục đầu tư này với phần mềm quản lý như Sparrow Wallet. seed của bạn sẽ luôn ngoại tuyến, vì chỉ phần công khai của danh mục đầu tư mới được truyền đến Sparrow. Điều này sẽ cho phép phần mềm hiển thị địa chỉ, giao dịch và tạo giao dịch mới mà không cần phải chi tiêu bitcoin của bạn. Để chi tiêu bitcoin, SeedSigner của bạn sẽ luôn phải ký giao dịch do Sparrow chuẩn bị.



### 6.1 Chuẩn bị SeedSigner



Lắp thẻ nhớ microSD chứa hệ điều hành, bật SeedSigner, sau đó tải mã seed bạn vừa tạo từ mã QR dự phòng. Trên màn hình chính, chọn `Quét`, sau đó quét SeedQR bằng SeedSigner.



![Image](assets/fr/046.webp)



Kiểm tra xem dấu vân tay trên chìa khóa chính của bạn có khớp với dấu vân tay trên wallet không. Nếu bạn đang sử dụng passphrase, hãy nhập dấu vân tay ở bước này.



![Image](assets/fr/047.webp)



Thao tác này sẽ đưa bạn đến menu danh mục đầu tư của bạn, trong trường hợp của tôi là `d4149b27`. Nếu bạn quay lại màn hình chính, hãy chọn `Seeds`, sau đó chọn bản in tương ứng với danh mục đầu tư của bạn. Sau đó, nhấp vào `Export Xpub`.



![Image](assets/fr/048.webp)



Chọn loại danh mục đầu tư. Trong trường hợp này, đó là danh mục đầu tư đơn lẻ: chọn `Single Sig`.



![Image](assets/fr/049.webp)



Tiếp theo là lựa chọn chuẩn kịch bản. Chuẩn mới nhất và tiết kiệm nhất về chi phí giao dịch là `Taproot`. Do đó, tôi khuyên bạn nên chọn chuẩn này.



![Image](assets/fr/050.webp)



Một thông báo cảnh báo sẽ xuất hiện. Điều này là bình thường: khóa công khai mở rộng (`xpub`) này cho phép bạn xem tất cả các địa chỉ được lấy từ seed của bạn (trên tài khoản đầu tiên). Nó không cho phép bạn chi tiêu tiền của mình, nhưng nó tiết lộ cấu trúc danh mục đầu tư của bạn. Nếu nó bị rò rỉ, đó sẽ là vấn đề đối với quyền riêng tư của bạn, nhưng không ảnh hưởng đến tính bảo mật của bitcoin: nó cho phép bạn xem chúng, nhưng không thể chi tiêu chúng.



Nhấp vào `Tôi hiểu`, sau đó nhấp vào `Xuất Xpub` nếu bạn hài lòng với thông tin hiển thị.



Sau đó, SeedSigner sẽ tạo xpub của bạn dưới dạng mã QR động chứa tất cả dữ liệu bạn cần để quản lý danh mục đầu tư của mình trong Sparrow Wallet.



![Image](assets/fr/051.webp)



Bạn có thể sử dụng cần điều khiển để điều chỉnh độ sáng màn hình để quét mã QR dễ dàng hơn.



### 6.2 Nhập danh mục đầu tư mới vào Sparrow Wallet



Hãy đảm bảo bạn đã cài đặt phần mềm Sparrow Wallet trên máy tính. Nếu bạn chưa biết cách tải xuống, kiểm tra và cài đặt đúng cách, hãy xem hướng dẫn đầy đủ của chúng tôi về chủ đề này:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Trên máy tính của bạn, hãy mở Sparrow Wallet, sau đó trên thanh menu, nhấp vào `File → Import Wallet`.



![Image](assets/fr/052.webp)



Cuộn xuống `SeedSigner`, sau đó chọn `Quét...`. Webcam của bạn sẽ mở ra: hãy quét mã QR động hiển thị trên màn hình SeedSigner.



![Image](assets/fr/053.webp)



Đặt tên cho danh mục đầu tư của bạn, sau đó nhấp vào `Tạo Wallet`. Sau đó, Sparrow sẽ yêu cầu bạn đặt mật khẩu để khóa quyền truy cập cục bộ vào wallet này. Hãy chọn một mật khẩu mạnh: mật khẩu này bảo vệ quyền truy cập vào dữ liệu danh mục đầu tư của bạn trong Sparrow (khóa công khai, địa chỉ, nhãn và lịch sử giao dịch). Không cần mật khẩu này để khôi phục danh mục đầu tư sau này: chỉ cần cụm từ ghi nhớ (và có thể cả passphrase) cho mục đích này.



Tôi khuyên bạn nên lưu mật khẩu này trong trình quản lý mật khẩu để tránh bị mất.



![Image](assets/fr/054.webp)



Kho khóa của bạn hiện đã được nhập thành công.



![Image](assets/fr/055.webp)



Sau đó kiểm tra xem `Dấu vân tay chính` hiển thị trong Sparrow có khớp với dấu vân tay đã ghi chú trước đó trong SeedSigner của bạn không.



SeedSigner và Sparrow Wallet của bạn hiện đã được liên kết an toàn. Sparrow hoạt động như một giao diện quản lý hoàn chỉnh, trong khi SeedSigner vẫn là thiết bị duy nhất có khả năng ký các giao dịch của bạn. Giờ đây, bạn đã sẵn sàng nhận và gửi bitcoin trong cấu hình air-gapped hoàn toàn.



## 7. Nhận và gửi bitcoin



SeedSigner và Sparrow Wallet của bạn hiện đã được cấu hình để hoạt động cùng nhau. Trong phần cuối cùng này, chúng ta sẽ xem xét cách nhận và gửi bitcoin bằng cấu hình này.



### 7.1 Nhận bitcoin



#### 7.1.1 Tạo địa chỉ tiếp nhận



Trên máy tính, hãy mở Sparrow Wallet và mở khóa SeedSigner wallet bằng mật khẩu của bạn. Đảm bảo phần mềm được kết nối với máy chủ (hình chữ V ở góc dưới bên phải). Trong thanh bên, nhấp vào `Nhận`.



![Image](assets/fr/056.webp)



Địa chỉ Bitcoin mới sẽ hiển thị. Bạn sẽ thấy:




- Địa chỉ văn bản (bắt đầu bằng `bc1p...` nếu bạn sử dụng P2TR như tôi),
- Mã QR tương ứng,
- Trường `Nhãn` để theo dõi giao dịch của bạn.



Tôi thực sự khuyên bạn nên thêm nhãn vào mỗi biên lai Bitcoin trên wallet của mình. Điều này sẽ giúp bạn dễ dàng xác định nguồn gốc của mỗi UTXO và cải thiện việc quản lý quyền riêng tư. Để tìm hiểu sâu hơn về chủ đề quan trọng này, bạn có thể xem chương trình đào tạo chuyên sâu trên Plan₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Để thêm nhãn, chỉ cần nhập tên vào trường `Nhãn`, sau đó xác nhận.



Ví dụ:



```txt
Label : Sale of the Raspberry Pi Zero
```



Địa chỉ của bạn hiện được liên kết với nhãn này trong tất cả các phần Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 Xác minh Address trên SeedSigner



Trước khi chia sẻ địa chỉ nhận, điều rất quan trọng là phải kiểm tra xem nó có thuộc về seed của bạn hay không. Bước này đảm bảo SeedSigner của bạn có thể ký các giao dịch liên quan đến địa chỉ này. Nó cũng bảo vệ chống lại các cuộc tấn công có thể xảy ra khi Sparrow hiển thị địa chỉ giả mạo. Hãy nhớ rằng Sparrow chạy trên một môi trường không an toàn (máy tính của bạn), có bề mặt tấn công lớn hơn nhiều so với SeedSigner của bạn, vốn hoàn toàn bị cô lập. Đó là lý do tại sao bạn không bao giờ nên tin tưởng mù quáng vào các địa chỉ nhận được hiển thị trên Sparrow cho đến khi bạn đã xác minh chúng bằng phần cứng wallet của mình.



Trên Sparrow, hãy nhấp vào mã QR của địa chỉ để phóng to: sau đó mã sẽ được hiển thị toàn màn hình.



![Image](assets/fr/058.webp)



Trên SeedSigner, từ menu chính, chọn `Quét`. Quét mã QR hiển thị trên màn hình máy tính, sau đó chọn seed tương ứng với wallet của bạn (trong trường hợp của tôi là dấu vân tay `d4149b27`).



![Image](assets/fr/059.webp)



Nếu địa chỉ được quét trùng khớp với địa chỉ lấy từ seed của bạn, màn hình SeedSigner sẽ hiển thị thông báo: `Address Verified`.



![Image](assets/fr/060.webp)



Điều này xác nhận rằng địa chỉ đó thuộc về wallet của bạn và bạn có thể tự tin nhận bitcoin từ đó.



#### 7.1.3 Nhận tiền



Bây giờ bạn có thể gửi địa chỉ này (dưới dạng văn bản hoặc mã QR) cho người hoặc bộ phận cần gửi satss cho bạn. Sau khi giao dịch được phát trên mạng, nó sẽ xuất hiện trong tab `Giao dịch` của Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Gửi bitcoin



Gửi bitcoin bằng SeedSigner là quy trình gồm 3 bước:




- Tạo giao dịch trong Sparrow;
- Chữ ký giao dịch trên SeedSigner;
- Phân phối cuối cùng của giao dịch thông qua Sparrow.



Mọi giao dịch giữa hai thiết bị đều được thực hiện hoàn toàn bằng mã QR.



#### 7.2.1 Tạo giao dịch trong Sparrow



Trong Sparrow Wallet, bạn có thể nhấp vào tab `Gửi` ở thanh bên trái. Tuy nhiên, tôi thích sử dụng tab `UTXOs` hơn, cho phép bạn thực hành "*Điều khiển Coin*". Phương pháp này cho phép bạn kiểm soát chính xác các UTXO được sử dụng, nhờ đó bạn có thể kiểm soát thông tin mình tiết lộ trong quá trình giao dịch.



Trong tab `UTXOs`, hãy chọn loại tiền bạn muốn chi tiêu, sau đó nhấp vào `Gửi loại tiền đã chọn`.



![Image](assets/fr/062.webp)



Sau đó điền vào các trường giao dịch:




- Trong `Thanh toán đến`, hãy dán địa chỉ người nhận hoặc nhấp vào biểu tượng máy ảnh để quét mã QR;
- Trong `Nhãn`, thêm nhãn để theo dõi khoản chi phí này;
- Trong `Số tiền`, nhập số tiền cần gửi;
- Cuối cùng, hãy chọn mức phí dựa trên điều kiện thị trường hiện tại (có thể tham khảo ước tính tại [mempool.space](https://mempool.space/)).



Sau khi đã hoàn tất các trường, hãy kiểm tra thông tin cẩn thận, sau đó nhấp vào `Tạo giao dịch >>`.



![Image](assets/fr/063.webp)



Kiểm tra thông tin chi tiết giao dịch để đảm bảo mọi thứ đều chính xác, sau đó nhấp vào `Hoàn tất giao dịch để ký`.



![Image](assets/fr/064.webp)



Giao dịch hiện đã sẵn sàng, nhưng chưa được ký. Để hiển thị [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) dưới dạng mã QR, hãy nhấp vào `Hiển thị QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Ký giao dịch với SeedSigner



Bật SeedSigner và quét SeedQR để truy cập danh mục đầu tư như bình thường. Từ màn hình chính, chọn `Quét`, sau đó quét mã QR hiển thị trên Sparrow.



![Image](assets/fr/066.webp)



Sau đó, hãy chọn seed phù hợp với danh mục đầu tư của bạn.



![Image](assets/fr/067.webp)



SeedSigner tự động phát hiện đây là PSBT và hiển thị tóm tắt giao dịch:




   - Số tiền đã gửi,
   - Địa chỉ đầu ra,
   - Chi phí giao dịch liên quan.



Nhấp vào `Xem lại Chi tiết` và kiểm tra kỹ tất cả thông tin trực tiếp trên màn hình SeedSigner. Những mục quan trọng nhất cần kiểm tra là số tiền đã gửi, địa chỉ người nhận và số tiền phí được áp dụng.



![Image](assets/fr/068.webp)



Nếu mọi thứ đều chính xác, hãy chọn `Phê duyệt PSBT` để ký giao dịch bằng khóa riêng tương ứng.



![Image](assets/fr/069.webp)



Sau khi ký, SeedSigner sẽ tạo mã QR mới chứa giao dịch đã ký, sẵn sàng để Sparrow quét.



![Image](assets/fr/070.webp)



#### 7.2.3 Phát sóng giao dịch từ Sparrow



Bây giờ giao dịch đã hợp lệ, nó cần được phát trên mạng Bitcoin để người khai thác có thể thêm giao dịch đó vào khối.



Trên Sparrow, nhấp vào `Quét QR`.



![Image](assets/fr/071.webp)



Trình bày mã QR được SeedSigner của bạn hiển thị (mã QR của giao dịch đã ký) cho webcam. Sparrow sẽ giải mã chữ ký và hiển thị đầy đủ chi tiết giao dịch. Kiểm tra lại lần cuối để đảm bảo tất cả thông tin đều chính xác, sau đó nhấp vào Phát Giao dịch để phát trên mạng Bitcoin.



![Image](assets/fr/072.webp)



Giao dịch của bạn hiện đã được gửi đến mạng lưới Bitcoin. Bạn có thể theo dõi tiến trình giao dịch trong tab `Giao dịch` của Sparrow Wallet.



![Image](assets/fr/073.webp)



Bây giờ bạn đã nắm vững những kiến thức cơ bản về cách sử dụng SeedSigner. Để hiểu sâu hơn và khám phá những cách sử dụng nâng cao hơn, tôi mời bạn tham khảo hướng dẫn sau:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Bạn cũng có thể hỗ trợ sự phát triển của dự án mã nguồn mở SeedSigner bằng cách quyên góp bằng bitcoin!](https://seedsigner.com/donate/)**



*Nguồn: một số hình ảnh trong hướng dẫn này được lấy từ [trang web chính thức của dự án SeedSigner](https://seedsigner.com/) và [kho lưu trữ GitHub](https://github.com/SeedSigner/seedsigner).*