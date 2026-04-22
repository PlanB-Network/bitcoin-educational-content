---
name: Bacca
description: Cấu hình Ledger mà không cần phần mềm Ledger Live
---
![cover](assets/cover.webp)


Nếu bạn sử dụng Ledger, có lẽ bạn đã nhận thấy rằng bạn phải sử dụng phần mềm Ledger Live, ít nhất là để cấu hình thiết bị ban đầu, kiểm tra tính xác thực và cài đặt ứng dụng Bitcoin lên đó. Tuy nhiên, sau khi cấu hình này, nhiều người dùng Bitcoin thích sử dụng phần mềm quản lý Bitcoin/wallet chuyên dụng như Sparrow hoặc Liana hơn là Ledger Live. Mặc dù Ledger sản xuất các thiết bị phần cứng wallet tuyệt vời, nhanh chóng tích hợp các tính năng mới nhất của Bitcoin, nhưng phần mềm của họ không nhất thiết phù hợp với nhu cầu cụ thể của người dùng Bitcoin. Thực tế, Ledger Live bao gồm nhiều tính năng được thiết kế cho các loại tiền điện tử khác (altcoin), trong khi các tùy chọn dành riêng cho việc quản lý Bitcoin/wallet lại bị hạn chế. Nhưng vấn đề với Sparrow và Liana (hiện tại) là chúng không cho phép bạn cài đặt ứng dụng Bitcoin trên Ledger.


Để bỏ qua bước sử dụng Ledger Live trong quá trình cấu hình ban đầu của Ledger, bạn có thể sử dụng công cụ Bacca (hay còn gọi là "Ledger Installer"). Phần mềm này cho phép bạn cài đặt và cập nhật ứng dụng Bitcoin, xác minh tính xác thực của Ledger, và thậm chí cập nhật firmware của thiết bị sau này. Bacca được tạo ra bởi Antoine Poinsot (Darosior), nhà phát triển cốt lõi của Bitcoin tại Chaincode Labs, đồng sáng lập [của Revault và Liana](https://wizardsardine.com/), và là một người dùng Pythcoin.


Trong hướng dẫn này, tôi sẽ chỉ cho bạn cách sử dụng công cụ này, để bạn có thể hoàn toàn không cần phần mềm Ledger Live nữa mà vẫn có thể tận hưởng các thiết bị Ledger. Công cụ này hoạt động trên tất cả các thiết bị: Nano S Classic, Nano S Plus, Nano X, Flex và Stax.


---
*Xin lưu ý rằng công cụ này khá mới và các nhà phát triển của nó cho biết rằng nó vẫn đang **trong giai đoạn thử nghiệm**. Họ khuyến nghị chỉ sử dụng nó cho mục đích thử nghiệm và không dùng cho thiết bị dự định lưu trữ Bitcoin hoặc wallet thực tế, mặc dù việc đó là có thể. Vì vậy, tôi khuyên bạn nên làm theo các khuyến nghị của các nhà phát triển công cụ này, được nêu rõ [trong tệp README của kho lưu trữ GitHub của họ](https://github.com/darosior/ledger_installer).*


---
## Điều kiện tiên quyết


Trên máy tính của bạn, bạn sẽ cần hai công cụ để sử dụng Bacca:




- Git;
- Rust.


Nếu bạn đã cài đặt chúng rồi thì có thể bỏ qua bước này.


**Linux:**


Trên các bản phân phối Linux, Git thường được cài đặt sẵn. Để kiểm tra xem Git đã được cài đặt trên hệ thống của bạn hay chưa, bạn có thể nhập lệnh sau vào terminal:


```bash
git --version
```


Nếu bạn chưa cài đặt Git trên hệ thống của mình, đây là lệnh để cài đặt nó trên Debian:


```bash
sudo apt install git
```


Cuối cùng, để cài đặt môi trường phát triển Rust, hãy sử dụng lệnh sau:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Windows:**


Để cài đặt Git, hãy truy cập [trang web chính thức của dự án](https://git-scm.com/). Tải xuống phần mềm và làm theo hướng dẫn cài đặt.


![BACCA](assets/fr/01.webp)


Hãy tiến hành theo cách tương tự để cài đặt Rust từ [trang web chính thức](https://www.rust-lang.org/tools/install).


![BACCA](assets/fr/02.webp)


**MacOS:**


Nếu Git chưa được cài đặt trên hệ thống của bạn, hãy mở cửa sổ dòng lệnh và chạy lệnh sau để cài đặt:


```bash
git --version
```


Nếu Git chưa được cài đặt trên hệ thống của bạn, một cửa sổ sẽ hiện ra đề nghị bạn cài đặt Xcode, trong đó có Git. Chỉ cần làm theo hướng dẫn trên màn hình để tiếp tục cài đặt.


Để cài đặt Rust, hãy chạy lệnh sau:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Lắp đặt Bacca


Mở cửa sổ dòng lệnh (terminal) và chuyển đến thư mục bạn muốn lưu phần mềm, sau đó chạy lệnh sau:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


Truy cập vào thư mục phần mềm:


```bash
cd ledger_installer
```


Sau đó sử dụng Cargo để biên dịch dự án và chạy giao diện người dùng đồ họa Bacca:


```bash
cargo run -p ledger_manager_gui
```


Giờ đây bạn đã có quyền truy cập vào giao diện phần mềm.


![BACCA](assets/fr/03.webp)


## Cấu hình Ledger


Trước khi bắt đầu, nếu Ledger của bạn là thiết bị mới, hãy đảm bảo bạn đã thiết lập mã PIN và lưu cụm từ khôi phục. Bạn không cần Ledger Live cho các bước ban đầu này. Chỉ cần kết nối Ledger của bạn qua cáp USB để cấp nguồn. Nếu bạn không chắc chắn cách thực hiện hai bước này, bạn có thể tham khảo phần đầu của hướng dẫn dành riêng cho kiểu máy của mình:




https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Sử dụng Bacca


Kết nối Ledger với máy tính của bạn và mở khóa bằng mã PIN bạn đã thiết lập. Bacca sẽ tự động nhận diện Ledger.


![BACCA](assets/fr/04.webp)


Để xác nhận tính xác thực của thiết bị Ledger, hãy nhấp vào nút "*Kiểm tra*". Bạn cần cấp quyền kết nối trên thiết bị Ledger để tiếp tục.


![BACCA](assets/fr/05.webp)


Bacca sẽ thông báo cho bạn biết Ledger của bạn có phải là hàng chính hãng hay không. Nếu không phải, điều này cho thấy thiết bị đã bị xâm nhập hoặc là hàng giả. Trong trường hợp này, hãy ngừng sử dụng ngay lập tức.


![BACCA](assets/fr/06.webp)


Trong menu "*Ứng dụng*", bạn có thể xem danh sách các ứng dụng đã được cài đặt trên Ledger của mình.


![BACCA](assets/fr/07.webp)


Để cài đặt ứng dụng Bitcoin, hãy nhấp vào "*Cài đặt*", sau đó cho phép cài đặt trên Ledger của bạn.


![BACCA](assets/fr/08.webp)


Ứng dụng đã được cài đặt thành công.


![BACCA](assets/fr/09.webp)


Nếu bạn chưa cài đặt phiên bản mới nhất của ứng dụng Bitcoin, Bacca sẽ hiển thị nút "*Cập nhật*" thay vì chỉ báo "*Mới nhất*". Chỉ cần nhấp vào nút này để cập nhật ứng dụng.


![BACCA](assets/fr/10.webp)


Giờ đây, khi Ledger của bạn đã được cấu hình chính xác với phiên bản ứng dụng Bitcoin mới nhất, bạn đã sẵn sàng nhập và sử dụng wallet trên các phần mềm quản lý như Sparrow hoặc Liana mà không cần phải thông qua Ledger Live!


Nếu bạn thấy hướng dẫn này hữu ích, tôi rất biết ơn nếu bạn để lại một biểu tượng ngón tay cái màu xanh lá cây bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn rất nhiều!


Tôi cũng khuyên bạn nên xem hướng dẫn này về GnuPG, hướng dẫn này giải thích cách kiểm tra tính toàn vẹn và tính xác thực của phần mềm trước khi cài đặt. Đây là một thao tác quan trọng, đặc biệt khi cài đặt phần mềm quản lý wallet như Liana hoặc Sparrow:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc