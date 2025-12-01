---
name: Dojo
description: Một nút Bitcoin nguồn mở cho quyền riêng tư và quyền tự chủ
---

![cover](assets/cover.webp)



*Hướng dẫn này dựa trên [tài liệu chính thức của Ashigaru](https://ashigaru.rs/docs/), mà tôi đã tiếp thu và mở rộng. Tôi đã viết lại tất cả các phần để rõ ràng hơn, bổ sung thêm các giải thích chi tiết, cũng như hình ảnh minh họa cho người mới bắt đầu, giúp việc cài đặt và sử dụng dễ hiểu hơn.*



---

Dojo là một chương trình nguồn mở được thiết kế để hoạt động như một máy chủ phụ trợ cho một số ví Bitcoin chú trọng quyền riêng tư, dựa trên một nút Bitcoin core. Trước đây, nó được phát triển để hoạt động với Samourai Wallet, một Wallet di động cung cấp các tính năng bảo mật nâng cao như Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet hiện đã bị ngừng hoạt động sau khi các nhà phát triển bị bắt, nhưng phiên bản kế nhiệm cộng đồng của nó, **Ashigaru Wallet**, đã tiếp quản và tiếp tục dựa vào Dojo để mang đến trải nghiệm toàn diện cho người dùng muốn kiểm soát dữ liệu của mình khi sử dụng Bitcoin.



![Image](assets/fr/01.webp)



Trên thực tế, Dojo hoạt động như một cổng kết nối giữa mạng Wallet và mạng Bitcoin của bạn. Nếu không có Dojo, một Wallet di động nhẹ sẽ phải truy vấn máy chủ của bên thứ ba để lấy trạng thái UTXO và lịch sử giao dịch của bạn, hoặc để phát sóng các giao dịch của bạn. Điều này đồng nghĩa với việc dữ liệu nhạy cảm sẽ bị phụ thuộc và rò rỉ sang máy chủ của bên thứ ba (địa chỉ được sử dụng, số tiền, tần suất thanh toán, v.v.). Với Dojo, bạn tự lưu trữ máy chủ này, được kết nối trực tiếp với nút Bitcoin của riêng bạn. Bằng cách này, tất cả các yêu cầu danh mục đầu tư của bạn sẽ đi qua một cơ sở hạ tầng do bạn kiểm soát, không qua trung gian, giúp tăng cường tính bảo mật và chủ quyền của bạn.



## Yêu cầu để thành lập một Dojo



Việc thiết lập máy chủ Dojo không yêu cầu cấu hình quá mạnh. Bất kỳ ai có máy tính cơ bản, kết nối Internet ổn định và khả năng hoạt động liên tục (24/7) đều có thể thiết lập một Dojo hoạt động.



### Chọn loại máy của bạn



Bạn có thể sử dụng:




- một máy tính xách tay;
- một máy tính để bàn;
- một máy tính mini (ví dụ: Intel NUC, Lenovo Thincentre Tiny...).



Mỗi lựa chọn đều có ưu và nhược điểm riêng:




- Giá cả: một chiếc máy tính mini hoặc máy tính để bàn tân trang thường sẽ rẻ hơn một chiếc máy tính xách tay mới.
- Dấu chân: Mini-PC chiếm ít không gian hơn.
- Power Supply: máy tính xách tay có ưu điểm là có pin, nghĩa là máy sẽ không tắt khi mất điện, không giống như máy tính mini.
- Khả năng nâng cấp: barbone thường cho phép bạn thêm bộ nhớ hoặc dễ dàng thay thế đĩa Hard.



Để biết thêm thông tin về cách lựa chọn thiết bị, tôi khuyên bạn nên tham gia khóa học này:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Thiết bị được đề xuất



Không cần phải mua máy mới. Một máy tính tân trang với các thông số kỹ thuật dưới đây sẽ có hiệu suất tốt hơn nhiều so với các thiết bị điện tử bo mạch đơn (như Raspberry Pi).



**Thông số kỹ thuật tối thiểu:**




- Kiến trúc X86-64 (bộ xử lý 64-bit).
- Bộ xử lý lõi kép 2 GHz hoặc nhanh hơn.
- RAM tối thiểu 8 GB.
- Ổ SSD NVMe 2 TB trở lên (để lưu trữ Blockchain của Bitcoin và các chỉ mục cần thiết).



**Hệ điều hành được đề xuất: **




- Bản phân phối dựa trên Debian, như Ubuntu 24.04 LTS.



**Thiết bị được khuyến nghị:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Máy tính cá nhân Intel NUC
- vân vân.



Hoàn toàn có thể chạy máy chủ Dojo trên các cấu hình phần cứng khác. Tuy nhiên, để có hiệu suất tốt nhất và hạn chế sự cố, chúng tôi khuyên bạn nên làm theo các khuyến nghị trên.



Trong hướng dẫn này, tôi sẽ sử dụng một máy ThinkCentre Tiny cũ với bộ xử lý Intel Pentium Dual-Core G4400T, RAM 8 GB và ổ SSD 2 TB.



## 1 - Cài đặt Ubuntu



*Nếu bạn muốn cài đặt Dojo trên thiết bị đã được cấu hình, bạn có thể bỏ qua bước này và chuyển thẳng sang bước 2.*



Sau khi đã chuẩn bị phần cứng, đã đến lúc cài đặt hệ điều hành. Bạn có thể sử dụng hầu như bất kỳ bản phân phối Debian nào, nhưng tôi khuyên bạn nên chọn phiên bản LTS của Ubuntu, vì nó hoàn toàn phù hợp với mục đích của chúng ta. Dưới đây là các bước cần thực hiện:



### 1.1. tạo một ổ USB có thể khởi động



Từ một máy tính đang hoạt động (máy tính bạn thường dùng), tải xuống ảnh ISO Ubuntu LTS [từ trang web chính thức](https://ubuntu.com/download/desktop) (`24.04` tại thời điểm viết bài, nhưng hãy lấy phiên bản mới nhất nếu có phiên bản khác).



![Image](assets/fr/02.webp)



Cắm một ổ USB có dung lượng tối thiểu 8 GB vào máy tính này, sau đó tạo một ổ USB có thể khởi động bằng phần mềm như [Balena Etcher](https://etcher.balena.io/). Chọn ảnh ISO Ubuntu bạn vừa tải xuống, chọn ổ USB làm thiết bị đích, sau đó bắt đầu quá trình tạo (hãy kiên nhẫn, quá trình này có thể mất vài phút).



![Image](assets/fr/03.webp)



Cắm ổ USB có thể khởi động vào máy tính đã tắt (máy tính bạn muốn chạy Dojo). Khởi động máy và ngay lập tức nhấn **F12** hoặc **F10** trên bàn phím (tùy thuộc vào kiểu máy) để truy cập menu khởi động. Sau đó, chọn ổ USB làm thiết bị ưu tiên trong thứ tự khởi động máy tính.



![Image](assets/fr/04.webp)



### 1.2. Cài đặt hệ điều hành



Màn hình chính của Ubuntu xuất hiện. Chọn "Dùng thử hoặc Cài đặt Ubuntu*".



![Image](assets/fr/05.webp)



Sau đó làm theo quy trình cài đặt Ubuntu cổ điển:




- Chọn ngôn ngữ.
- Chọn loại bàn phím.
- Nếu bạn kết nối qua cáp RJ45, bạn không cần phải cấu hình Wi-Fi.
- Nhấp vào "*Cài đặt Ubuntu*" và chọn tùy chọn cài đặt phần mềm của bên thứ ba (trình điều khiển Wi-Fi, codec đa phương tiện, v.v.).
- Khi trình hướng dẫn hỏi loại cài đặt, hãy chọn "*Xóa đĩa và cài đặt Ubuntu*". **Cảnh báo**: Thao tác này sẽ xóa hoàn toàn nội dung của đĩa. Hãy kiểm tra cẩn thận xem đĩa bạn đã chọn có tương ứng với ổ SSD NVMe dành cho Dojo không.
- Tạo một tên người dùng đơn giản (ví dụ: "*loic*").
- Đặt tên cho máy (ví dụ: "*dojo-node*").
- Đặt mật khẩu mạnh và giữ an toàn.
- Bật tùy chọn "*Yêu cầu mật khẩu để đăng nhập*" để tăng cường bảo mật.
- Chỉ định múi giờ của bạn, sau đó nhấp vào "*Cài đặt*".
- Đợi quá trình cài đặt hoàn tất. Sau khi hoàn tất, hệ thống sẽ tự động khởi động lại.
- Tháo khóa cài đặt USB khi khởi động lại máy tính.



Để biết thêm chi tiết về quy trình cài đặt Ubuntu, vui lòng xem hướng dẫn chuyên dụng của chúng tôi:



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. cập nhật hệ thống



Sau lần khởi động đầu tiên, hãy mở terminal bằng tổ hợp phím ***Ctrl + Alt + T*** và chạy các lệnh sau để cập nhật hệ thống:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Lắp đặt nhà phụ



Để Dojo hoạt động bình thường, hệ thống của bạn phải có một số khối phần mềm nhất định. Chúng được sử dụng để quản lý kho phần mềm, giao tiếp, giải nén tệp và thực thi Dojo bên trong các container Docker. Tất cả các thao tác này đều được thực hiện trong terminal.



### 2.1. Chuẩn bị



Lệnh sau sẽ đưa bạn trở về thư mục cá nhân. Đây là một thao tác nên thực hiện trước khi chạy một loạt cài đặt.



```bash
cd ~/
```



Trước khi cài đặt bất kỳ phần mềm nào, hãy đảm bảo cơ sở dữ liệu phần mềm có sẵn trên máy của bạn được cập nhật. Điều này tránh cài đặt các phiên bản lỗi thời.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. Cài đặt tiện ích



Một số công cụ cần được thêm vào hệ thống:




- `apt-transport-https`: cho phép bạn tải xuống các gói tin một cách an toàn qua HTTPS
- `ca-certificates`: quản lý các chứng chỉ cần thiết cho các kết nối được mã hóa
- `curl`: để lấy các tập tin từ Internet
- `gnupg-agent`: để quản lý khóa GPG
- software-properties-common`: cung cấp các tiện ích để thao tác kho lưu trữ APT
- `unzip`: giải nén các tập tin ở định dạng ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Trong quá trình cài đặt, hệ thống có thể yêu cầu bạn xác nhận. Nhấn phím "*y*", sau đó nhấn "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. cài đặt Torsocks



Torsocks cho phép thực hiện một số lệnh nhất định thông qua mạng Tor, cải thiện tính bảo mật của thông tin liên lạc.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. Cài đặt Docker và Docker Compose



Dojo chạy bên trong các container Docker. Điều này có nghĩa là mỗi dịch vụ được cô lập trong một môi trường độc lập, giúp đơn giản hóa việc bảo trì và bảo mật. Để làm được điều này, bạn cần cài đặt Docker và công cụ Docker Compose, cho phép bạn quản lý nhiều container cùng lúc.



#### Thêm khóa ký Docker



Docker cung cấp khóa chữ ký số riêng. Việc thêm khóa này sẽ xác minh tính xác thực của các gói đã tải xuống.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Đã thêm kho lưu trữ Docker chính thức



Tiếp theo, bạn cần cho hệ thống biết nơi tìm các gói Docker chính thức. Lệnh này sẽ thêm một kho lưu trữ mới vào cấu hình trình quản lý gói của bạn.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Cài đặt Docker và Docker Compose



Các thành phần chính của Docker hiện có thể được cài đặt.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Quyền hạn người dùng



Theo mặc định, chỉ những lệnh được thực hiện với quyền quản trị viên mới có thể khởi chạy Docker. Để thuận tiện hơn, tôi khuyên bạn nên thêm người dùng hiện tại vào nhóm "*docker*". Điều này cho phép bạn sử dụng Docker mà không cần phải gõ `sudo` mỗi lần.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Tạo người dùng đơn lẻ (tùy chọn)



Nếu bạn muốn cải thiện bảo mật hệ thống, tôi khuyên bạn nên tạo một người dùng riêng biệt chỉ để chạy Dojo. Việc phân tách này sẽ hạn chế rủi ro: nếu xảy ra sự cố bảo mật trong Dojo, nó sẽ không ảnh hưởng trực tiếp đến tài khoản chính của bạn.



### 3.1. tạo tài khoản người dùng



Lệnh sau sẽ tạo một người dùng mới tên là "*dojo*". Người dùng này sẽ có thư mục home `/home/dojo` và quyền truy cập vào terminal bash. Người dùng này cũng sẽ được thêm vào nhóm sudo để cho phép thực thi các lệnh quản trị.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Thiết lập mật khẩu



Điều quan trọng là phải đặt mật khẩu mạnh cho tài khoản này. Lý tưởng nhất là bạn nên sử dụng trình quản lý mật khẩu như Bitwarden để tạo một chuỗi ký tự dài generate, trong đó Hard là một chuỗi ký tự khó đoán.



```bash
sudo passwd dojo
```



Sau đó, hệ thống sẽ yêu cầu bạn nhập mật khẩu đã chọn, sau đó xác nhận lại lần thứ hai.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Cho phép người dùng sử dụng Docker



Để cho phép người dùng "*dojo*" khởi chạy các container cần thiết để chạy Dojo, người dùng đó phải được thêm vào nhóm Docker. Điều này giúp tránh phải thêm lệnh `sudo` vào trước mỗi lệnh.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Khởi động lại hệ thống



Để những thay đổi của nhóm có hiệu lực, máy phải được khởi động lại.



```bash
sudo reboot
```



### 3.5. Đăng nhập bằng người dùng mới



Khi hệ thống khởi động lại, hãy đăng nhập bằng tài khoản ***dojo*** và mật khẩu bạn đã thiết lập trước đó. Tất cả các bước tiếp theo phải được thực hiện từ tài khoản chuyên dụng này.



## 4. Tải xuống và kiểm tra Dojo



Trước khi cài đặt Dojo, điều quan trọng là phải đảm bảo các tệp đến từ nhà phát triển chính thức và chưa bị chỉnh sửa. Bước này dựa trên việc sử dụng PGP và hàm băm để xác minh tính xác thực và toàn vẹn của tệp.



### 4.1. nhập khóa PGP của nhà phát triển



Tải xuống khóa công khai của nhà phát triển qua Tor và nhập nó vào keychain cục bộ của bạn. Khóa này sẽ được sử dụng để xác minh chữ ký liên quan đến các tệp Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. Tải xuống phiên bản mới nhất của Dojo



Truy xuất tệp nén chứa mã nguồn Dojo. Trong ví dụ này, phiên bản mới nhất là `1.27.0`: hãy sửa đổi lệnh theo [phiên bản mới nhất tại kho lưu trữ GitHub chính thức](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Tải xuống dấu vân tay và chữ ký



Các nhà phát triển đã xuất bản một tệp liệt kê dấu vân tay kỹ thuật số của các kho lưu trữ, cũng như một tệp được ký bằng khóa PGP của họ. Hãy tải xuống để so sánh các tệp của bạn tại địa phương.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Kiểm tra chữ ký PGP



Kiểm tra xem tệp dấu vân tay đã được ký bằng khóa đã nhập chưa.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Kết quả chính xác sẽ hiển thị chữ ký hợp lệ với khóa `E53AD419B242822F19E23C6D3033D463D6E544F6` và Address `dojocoder@pm.me` được liên kết. Một cảnh báo có thể xuất hiện cho biết khóa chưa được chứng thực: bạn có thể bỏ qua.



Ngược lại, nếu chữ ký không hợp lệ, hãy dừng ngay quá trình cài đặt và bắt đầu lại từ đầu.



![Image](assets/fr/17.webp)



### 4.5. Kiểm tra tính toàn vẹn của kho lưu trữ



Tính toán dấu vân tay SHA256 của tệp đã tải xuống, sau đó mở tệp dấu vân tay để so sánh hai giá trị.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Nếu hai dấu vân tay giống hệt nhau, bạn có thể chắc chắn rằng tệp lưu trữ chưa bị chỉnh sửa. Nếu chúng khác nhau, hãy xóa các tệp đó.



![Image](assets/fr/18.webp)



### 4.6. Trích xuất và sắp xếp các tập tin



Sau khi xác minh thành công, bạn có thể giải nén tệp lưu trữ và chuẩn bị một thư mục dành riêng cho việc cài đặt Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Dọn dẹp các tập tin không cần thiết



Xóa các tệp tạm thời và kho lưu trữ không còn cần thiết để giữ cho môi trường của bạn sạch sẽ.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Cấu hình Dojo



Dojo là một máy chủ back-end kết hợp nhiều dịch vụ để tương tác với danh mục đầu tư của bạn và quản lý nút Bitcoin. Cấu hình của Dojo có thể phức tạp, nhưng dự án cung cấp một phương pháp đơn giản hóa, tự động cài đặt và cấu hình các thành phần sau:




- Dojo (API chính)
- Bitcoin core (nút Bitcoin hoàn chỉnh)
- Trình khám phá BTC-RPC (web Block explorer)
- Fulcrum Indexer (lập chỉ mục nhanh các khối và giao dịch)
- Máy chủ Fulcrum Electrum có sẵn trên mạng Tor
- Máy chủ Fulcrum Electrum có sẵn trên mạng cục bộ
- Giấy chứng nhận quản trị



### 5.1. thông tin quản trị



Để bảo mật quyền truy cập vào các dịch vụ khác nhau, bạn cần generate một số mã định danh duy nhất:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- người dùng mySQL
- `MẬT KHẨU MYSQL`
- Khóa API nODE`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Những mã định danh này **phải là duy nhất** (điều này rất quan trọng: bạn không được sử dụng cùng một mật khẩu cho nhiều dịch vụ), chỉ bao gồm số, chữ in hoa và chữ thường (chữ và số), và dài khoảng 40 ký tự để đảm bảo mức độ bảo mật cao. Một lần nữa, tôi thực sự khuyên bạn nên sử dụng trình quản lý mật khẩu.



### 5.2. Truy cập các tập tin cấu hình



Các tệp cấu hình Dojo nằm trong thư mục `conf/`. Di chuyển đến thư mục này:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Cấu hình Bitcoin core



Mở tệp cấu hình Bitcoin core bằng trình soạn thảo văn bản nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



Trong tệp này, hãy nhập các mã định danh đã tạo:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Thay thế `your-ID-here` và `your-password-here` bằng thông tin đăng nhập của riêng bạn (với mật khẩu mạnh).***



Bạn cũng có thể điều chỉnh kích thước bộ nhớ đệm được Bitcoin core sử dụng để cải thiện hiệu suất (bạn thậm chí có thể sử dụng nhiều hơn nếu có nhiều RAM):



```
BITCOIND_DB_CACHE=2048
```



Để lưu thay đổi và đóng trình soạn thảo:




- nhấn `Ctrl + X
- gõ `y`
- sau đó nhấn "*Enter*"



### 5.4. Cấu hình MySQL



Sau đó mở cấu hình cơ sở dữ liệu MySQL:



```bash
nano docker-mysql.conf.tpl
```



Vui lòng nhập thông tin đăng nhập của bạn:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Thay thế `your-ID-here` và `your-password-here` bằng thông tin đăng nhập của riêng bạn (với mật khẩu mạnh và duy nhất).***



Lưu theo cách tương tự (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Cấu hình chỉ mục Fulcrum



Mở tệp sau:



```bash
nano docker-indexer.conf.tpl
```



Thêm các tham số để kích hoạt Fulcrum và tích hợp chính xác vào Dojo:



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Tiếp theo, có 2 khả năng, tùy thuộc vào cấu hình của bạn. Nếu Dojo được cài đặt trên một máy tính riêng biệt với máy tính thường ngày của bạn (trên một máy chuyên dụng, máy chủ...), hãy nhập IP Address của nó vào mạng cục bộ, ví dụ:



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Để tìm ra địa chỉ IP cục bộ Address của máy bạn, hãy mở một thiết bị đầu cuối khác và nhập lệnh sau:



```bash
hostname -I
```



Khả năng thứ hai: nếu Dojo được chạy trực tiếp trên máy tính cá nhân thường ngày của bạn, hãy giữ nguyên giá trị mặc định có trong tệp cấu hình:



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Lưu và thoát khỏi trình soạn thảo (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Cấu hình dịch vụ nút



Cuối cùng, hãy mở cấu hình của dịch vụ Dojo chính:



```bash
nano docker-node.conf.tpl
```



Vui lòng nhập thông tin đăng nhập của bạn:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Thay thế `your-password-here` bằng thông tin đăng nhập của bạn (với mật khẩu mạnh và duy nhất).***



![Image](assets/fr/26.webp)



Sau đó kích hoạt trình lập chỉ mục cục bộ:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Lưu và thoát khỏi trình soạn thảo (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Quản lý đăng nhập



Sau khi cấu hình xong, không cần phải lưu tất cả các mã định danh đã tạo. Mã định danh duy nhất bắt buộc phải lưu là:



```
NODE_ADMIN_KEY
```



Đăng nhập này sẽ cho phép bạn đăng nhập vào công cụ bảo trì Dojo sau này. Tất cả các thông tin đăng nhập khác có thể được xóa khỏi trình quản lý mật khẩu hoặc ghi chú viết tay của bạn. Bạn vẫn có thể truy cập chúng từ các tệp cấu hình Dojo nếu cần khôi phục sau này.



## 6. Cài đặt Dojo



Ở giai đoạn này, Dojo sẽ được cài đặt và khởi động trên máy của bạn. Thao tác này sẽ khởi chạy một số dịch vụ (Bitcoin core, trình lập chỉ mục Fulcrum, phần mềm quản lý Dojo, v.v.) và bắt đầu đồng bộ hóa hoàn toàn Blockchain Bitcoin. Quá trình này có thể mất vài ngày, tùy thuộc vào phần cứng và kết nối Internet của bạn.



### 6.1. Kiểm tra xem Docker có hoạt động bình thường không



Trước khi bắt đầu cài đặt, hãy đảm bảo Docker đang hoạt động. Chạy lệnh sau:



```bash
docker run hello-world
```



Lệnh này sẽ tải xuống và khởi chạy một container thử nghiệm nhỏ. Nếu mọi thứ hoạt động bình thường, bạn sẽ thấy thông báo tương tự như sau:



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Nếu thông báo này không hiển thị, hãy bắt đầu bằng cách khởi động lại máy của bạn bằng:



```bash
sudo reboot
```



Sau đó, hãy đăng nhập lại vào tài khoản **dojo** của bạn và chạy lại lệnh kiểm tra. Nếu lỗi vẫn còn, Docker chưa được cài đặt đúng cách. Trong trường hợp này, hãy quay lại bước `2.4.` khi cài đặt Docker và kiểm tra kỹ từng lệnh.



### 6.2. Vào thư mục cài đặt Dojo



Các tập lệnh cần thiết để cài đặt nằm trong thư mục `my-dojo`. Di chuyển đến thư mục này:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Sử dụng lệnh `ls` để kiểm tra xem tệp `dojo.sh` đã có chưa. Đây là tập lệnh chính tự động cài đặt Dojo và khởi chạy tất cả các dịch vụ của nó.



![Image](assets/fr/29.webp)



### 6.3. Bắt đầu cài đặt



Bắt đầu cài đặt bằng cách chạy:



```bash
./dojo.sh install
```



Xác nhận cài đặt bằng cách nhấn `y` rồi nhấn "*Enter*".



![Image](assets/fr/30.webp)



Tập lệnh này sẽ:




- tải xuống và khởi chạy các container Docker cần thiết,
- khởi tạo Bitcoin core và bắt đầu đồng bộ hóa Blockchain,
- bắt đầu lập chỉ mục Fulcrum để theo dõi các giao dịch và địa chỉ,
- kích hoạt phần phụ trợ Dojo và các API của nó.



Bạn sẽ thấy một luồng nhật ký liên tục cuộn qua, với các tham chiếu đầy màu sắc như `bitcoind`, `soroban`, `nodejs` hoặc `fulcrum`. Việc cuộn này cho biết Dojo đã hoạt động và bắt đầu thực thi các dịch vụ khác nhau.



![Image](assets/fr/31.webp)



### 6.4. Hiển thị nhật ký thoát



Nhật ký sẽ xuất hiện theo thời gian thực trên terminal của bạn. Để quay lại dấu nhắc lệnh trong khi Dojo đang chạy nền, hãy nhập:



```
Ctrl + C
```



Đừng lo lắng: việc dừng hiển thị nhật ký không dừng các dịch vụ. Docker vẫn tiếp tục chạy Dojo ở chế độ nền (rõ ràng là bạn không cần phải dừng máy tính nếu muốn IBD tiếp tục).



### 6.5. Hiểu về *Tải xuống khối ban đầu* (IBD)



Khi khởi động, Bitcoin core phải tải xuống và xác minh toàn bộ Blockchain kể từ năm 2009. Bước này được gọi là ***Tải xuống Khối Ban đầu* (IBD)**. Bước này rất quan trọng vì nó cho phép nút Dojo của bạn xác minh từng khối và giao dịch Bitcoin một cách độc lập.



Thời gian đồng bộ hóa này phụ thuộc vào một số yếu tố:




- sức mạnh của bộ xử lý và dung lượng bộ nhớ RAM khả dụng,
- tốc độ đĩa của bạn,
- số lượng và chất lượng của các đối tác mà nút của bạn kết nối tới,
- tốc độ kết nối Internet của bạn.



Trên thực tế, thao tác này thường mất từ **2 đến 7 ngày**. Trong thời gian này, bạn có thể để máy chạy liên tục. Máy chạy càng lâu, quá trình đồng bộ hóa sẽ hoàn tất càng nhanh. Tôi khuyên bạn nên thường xuyên kiểm tra trạng thái đồng bộ hóa bằng cách tham khảo nhật ký Bitcoin core hoặc sử dụng công cụ bảo trì Dojo sau khi cài đặt (xem phần tiếp theo).



Để hiểu sâu hơn về bệnh IBD và nói chung là về hoạt động và vai trò của hạch Bitcoin, tôi khuyên bạn nên tham khảo khóa học này:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Giám sát đồng bộ hóa



Khi cài đặt Dojo lần đầu tiên, bạn cần chờ hai thao tác chính hoàn tất: tải xuống hoàn toàn Blockchain Bitcoin (*IBD*) và Fulcrum lập chỉ mục Blockchain này. Tùy thuộc vào kết nối và công suất máy tính của bạn, quá trình này có thể mất vài ngày. Trong thời gian này, bạn có thể theo dõi tiến trình để đảm bảo mọi thứ hoạt động trơn tru.



Có hai cách để theo dõi trạng thái đồng bộ hóa:




- sử dụng Công cụ bảo trì Dojo (hay DMT), công cụ này đơn giản nhưng cung cấp ít thông tin chi tiết trong quá trình IBD;
- tham khảo trực tiếp nhật ký Dojo trên máy của bạn, mang tính kỹ thuật hơn nhưng chính xác hơn nhiều.



### 7.1. Kiểm tra thông qua Công cụ bảo trì Dojo (DMT)



Công cụ Bảo trì Dojo là một Interface an toàn, hoạt động trên nền tảng web, cho phép bạn theo dõi trạng thái của nhà máy và thực hiện một số thao tác nhất định. Đây là cách dễ dàng và dễ tiếp cận nhất để theo dõi tiến trình của IBD. Trong giai đoạn đồng bộ hóa ban đầu, thông tin hiển thị có thể bị hạn chế. Ví dụ: DMT không hiển thị tiến trình lập chỉ mục Fulcrum chi tiết. Mặt khác, sau khi đồng bộ hóa hoàn tất, DMT sẽ hiển thị rõ ràng:




- tất cả đèn đều sáng Green;
- khối được xác thực cuối cùng cho mỗi dịch vụ (Node, Indexer, Dojo DB).



Để truy cập, bạn cần biết URL của DMT và kết nối với nó [thông qua trình duyệt Tor](https://www.torproject.org/download/). Để thực hiện việc này, hãy mở terminal và đi đến thư mục `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Sau đó chạy lệnh sau:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Sau đó, bạn sẽ có quyền truy cập vào tất cả thông tin liên quan đến kết nối đến Dojo của mình qua Tor. Đường dẫn chúng tôi quan tâm ở đây là URL sau:



```
Dojo API and Maintenance Tool =
```



Để truy cập DMT từ bất kỳ máy nào trên bất kỳ mạng nào (kể cả từ xa), hãy mở Trình duyệt Tor và nhập URL này theo sau là `/admin`. Ví dụ: nếu URL của bạn là `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, bạn sẽ cần nhập vào thanh [Trình duyệt Tor](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Vui lòng giữ bí mật tuyệt đối thông tin Address này



Sau đó, bạn sẽ được chuyển hướng đến trang xác thực. DMT sẽ được đăng nhập bằng mật khẩu `NODE_ADMIN_KEY` mà bạn đã tạo trước đó.



![Image](assets/fr/33.webp)



Sau khi đăng nhập, bạn có thể truy cập *Công cụ Bảo trì Dojo*! Trong quá trình IBD, bạn có thể xem thông tin "*Khối Mới nhất*" trong menu "*Full node*", cho bạn biết trạng thái hiện tại của nút Bitcoin.



![Image](assets/fr/34.webp)



Hãy nhớ đánh dấu trang Address này trong Tor Browser để dễ dàng truy xuất sau này.



Sau khi Dojo của bạn được đồng bộ hóa hoàn toàn, bạn sẽ thấy Green check ✅ trên tất cả các chỉ báo trên trang chủ DMT.



### 7.2. Xác minh thông qua nhật ký Dojo



Cách thứ hai để theo dõi tiến trình IBD của bạn là tham khảo trực tiếp nhật ký máy. Cách này cung cấp khả năng giám sát chính xác hơn nhiều theo thời gian thực. Bạn có thể thấy Bitcoin core đang tải xuống các khối như thế nào và Fulcrum đang lập chỉ mục chúng ra sao.



Kết nối với máy chủ Dojo của bạn và mở terminal. Tất cả các lệnh nên được thực thi từ thư mục `my-dojo`. Vào thư mục này:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Nhật ký Bitcoin core



Xem nhật ký Bitcoin core để theo dõi tiến trình của IBD:



```bash
./dojo.sh logs bitcoind
```



Lúc đầu, bạn sẽ thấy giai đoạn đồng bộ hóa trước của tiêu đề khối:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Khi con số này đạt 100%, Bitcoin core sẽ bắt đầu tải xuống hoàn toàn Blockchain. Bạn sẽ thấy tiến trình IBD. Để biết chiều cao khối hiện tại, hãy xem giá trị được chỉ định bởi `height=`. Bạn cũng có thể theo dõi khóa `progress=`, cho biết tỷ lệ phần trăm tiến trình IBD.



![Image](assets/fr/36.webp)



Như thường lệ, để đóng nhật ký và quay lại dấu nhắc lệnh, hãy sử dụng tổ hợp phím `Ctrl + C`.



#### Nhật ký Fulcrum



Sau khi Bitcoin core hoàn tất quá trình đồng bộ hóa tiêu đề trước, Fulcrum sẽ bắt đầu lập chỉ mục Blockchain trong quá trình hoạt động. Xem nhật ký của nó bằng cách:



```bash
./dojo.sh logs fulcrum
```



Sau đó, bạn sẽ thấy chiều cao của khối được lập chỉ mục cuối cùng, được chỉ ra sau `height:`, cũng như phần trăm tiến trình lập chỉ mục.



![Image](assets/fr/37.webp)



### 7.3. Hỏng cơ sở dữ liệu Fulcrum



Fulcrum là một công cụ lập chỉ mục đặc biệt mạnh mẽ, nhưng việc cài đặt nó có thể phức tạp, một phần do hệ thống quản lý cơ sở dữ liệu tinh vi của nó. Trong trường hợp mất điện hoặc máy tính đột ngột tắt trong quá trình đồng bộ hóa ban đầu, cơ sở dữ liệu của công cụ lập chỉ mục có thể bị hỏng. Ví dụ, bạn có thể thấy điều này nếu có các nhật ký sau:



```bash
fulcrum | The database has been corrupted etc...
```



**Lưu ý:** Loại lỗi này sẽ được sửa trong phiên bản Fulcrum 2.0 sắp tới.



Nếu điều này xảy ra với bạn, sẽ không có ảnh hưởng gì đến bitcoind (nút Bitcoin của bạn): IBD của nó sẽ tiếp tục hoạt động độc lập với Fulcrum. Tuy nhiên, bạn sẽ không thể sử dụng Fulcrum cho đến khi bạn xóa dữ liệu bị hỏng và khởi động lại quá trình đồng bộ hóa từ đầu. Cách thức hoạt động như sau:



Dừng Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Chỉ xóa vùng chứa và ổ đĩa Fulcrum:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Thông thường tên là `my-dojo_data-fulcrum`, nếu bạn không phải là người như vậy, hãy sử dụng tên được trả về bởi lệnh trước đó.



Sau đó khởi động lại Dojo và xây dựng lại Fulcrum từ đầu:



```bash
./dojo.sh upgrade
```



Sau đó, bạn có thể kiểm tra xem Fulcrum có hoạt động bình thường không bằng cách tham khảo nhật ký:



```bash
docker logs -f fulcrum
```




## 8. Sử dụng Công cụ Bảo trì Dojo



Khi nút thắt Bitcoin của bạn được đồng bộ hóa với đầu sợi dọc có Proof of Work nhiều nhất và Blockchain được Fulcrum lập chỉ mục 100%, bạn có thể bắt đầu sử dụng Dojo.



Dojo của bạn cung cấp nhiều tính năng đa dạng, được cải tiến thường xuyên qua mỗi phiên bản mới. Theo tôi, 2 tính năng quan trọng nhất là:




- khả năng kết nối Ashigaru Wallet của bạn để sử dụng nút riêng của bạn để tham khảo dữ liệu Blockchain và phát các giao dịch của bạn,
- và Block explorer, cho phép bạn truy cập thông tin về Blockchain Bitcoin mà không cần tiết lộ dữ liệu của bạn cho một thực thể bên ngoài mà bạn không kiểm soát.



Hãy cùng tìm hiểu cách sử dụng chúng nhé.


### 8.1. Kết nối Ashigaru với Dojo của bạn



Việc kết nối Ashigaru Wallet với Dojo rất đơn giản: sau khi kết nối DMT, hãy mở menu "*Ghép nối*". Một mã QR sẽ xuất hiện, bạn có thể quét trực tiếp bằng ứng dụng Ashigaru.



![Image](assets/fr/38.webp)



Trong ứng dụng Ashigaru, lần đầu tiên bạn khởi chạy sau khi tạo hoặc khôi phục Wallet, bạn sẽ được chuyển hướng đến trang "*Cấu hình máy chủ Dojo*". Nhấn "*Quét QR*", sau đó quét mã QR hiển thị trên DMT của bạn.



![Image](assets/fr/39.webp)



Sau đó nhấp vào nút "*Tiếp tục*".



![Image](assets/fr/40.webp)



Bây giờ bạn đã kết nối với Dojo của mình.



![Image](assets/fr/41.webp)



### 8.2. Sử dụng Block explorer



Dojo tự động cài đặt Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), sử dụng trực tiếp dữ liệu từ nút Bitcoin của bạn. Trình khám phá cho phép bạn truy cập thông tin thô từ Blockchain và Mempool của bạn thông qua giao diện web Interface dễ hiểu. Ví dụ, bạn có thể kiểm tra trạng thái của một giao dịch đang chờ xử lý, xem số dư của Address hoặc kiểm tra thành phần của một khối một cách dễ dàng.



Để truy cập, chỉ cần tải Tor Address từ trình duyệt của bạn. Để thực hiện việc này, hãy chạy cùng lệnh bạn đã dùng để tải Address của DMT:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Bạn sẽ có thể truy cập tất cả thông tin kết nối Dojo của mình thông qua Tor. Thông tin chúng tôi quan tâm ở đây là URL sau:



```
Block Explorer =
```



Nếu bạn đã kết nối với DMT, bạn cũng có thể tìm thấy Address này trong menu "*Ghép nối*", bên trong JSON kết nối:



![Image](assets/fr/43.webp)



Để truy cập trình duyệt của bạn từ bất kỳ máy nào trên bất kỳ mạng nào (kể cả từ xa), hãy mở [Trình duyệt Tor](https://www.torproject.org/download/) và nhập URL bạn vừa tải xuống.



⚠️ **Vui lòng giữ bí mật tuyệt đối thông tin Address này



Sau đó, bạn sẽ có quyền truy cập vào Block explorer của riêng mình.



![Image](assets/fr/44.webp)



*Nguồn hình ảnh: https://ashigaru.rs/.*



Để theo dõi giao dịch, chỉ cần nhập txid vào thanh tìm kiếm ở góc trên bên phải.



![Image](assets/fr/45.webp)



*Nguồn hình ảnh: https://ashigaru.rs/.*



Để kiểm tra các chuyển động liên quan đến Address, hãy tiến hành theo cách tương tự bằng cách nhập Address vào thanh tìm kiếm.



![Image](assets/fr/46.webp)



*Nguồn hình ảnh: https://ashigaru.rs/.*



Bạn cũng có thể nhập Hash hoặc chiều cao của khối vào thanh tìm kiếm để hiển thị thông tin chi tiết.



![Image](assets/fr/47.webp)



*Nguồn hình ảnh: https://ashigaru.rs/.*



## 9. Bảo trì Dojo



### 9.1 Dừng Dojo của bạn



Không bao giờ ngắt nguồn Dojo đột ngột, vì điều này có thể làm hỏng một số cơ sở dữ liệu, đặc biệt là bộ lập chỉ mục Fulcrum. Nếu bạn phải tắt Dojo, hãy luôn tắt Dojo hoàn toàn, sau đó, sau khi hoàn tất tất cả các quy trình, hãy tắt máy:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Cập nhật Dojo của bạn



Dojo liên tục phát triển và các phiên bản mới được phát hành để sửa lỗi, cải thiện tính ổn định và bổ sung tính năng. Do đó, việc thường xuyên kiểm tra các bản cập nhật (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) và cập nhật Dojo của bạn là rất quan trọng. Quy trình này tương tự như cài đặt ban đầu, nhưng yêu cầu bạn thay thế một số tệp bằng phiên bản mới nhất hiện có, đồng thời duy trì cấu hình. Dưới đây là các bước chi tiết cần thực hiện để có một bản cập nhật sạch sẽ và an toàn:



Để biết phiên bản hiện tại của Dojo, hãy chạy lệnh:



```bash
./dojo.sh version
```



Mặc dù bước này là tùy chọn, tôi khuyên bạn nên bắt đầu bằng việc cập nhật hệ điều hành. Việc này sẽ giảm thiểu nguy cơ không tương thích và đảm bảo các phần mềm phụ thuộc mà Dojo sử dụng luôn được cập nhật:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Vào thư mục Dojo và dừng các dịch vụ hiện tại:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Sau đó khởi động lại hệ thống để có lại trạng thái ban đầu:



```bash
sudo reboot
```



Dojo đi kèm với các tệp được ký số. Các chữ ký PGP này đảm bảo rằng các tệp có nguồn gốc từ nhà phát triển và không bị thay đổi dưới bất kỳ hình thức nào. Điều quan trọng là phải kiểm tra chúng mỗi khi bạn cập nhật Dojo, giống như khi bạn cài đặt lần đầu. Hãy bắt đầu bằng cách tải xuống khóa công khai của nhà phát triển qua Tor, sau đó nhập khóa đó:



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Trở về thư mục cá nhân của bạn:



```bash
cd ~/
```



Tải xuống phiên bản Dojo mới nhất từ GitHub qua Tor. Trong ví dụ này, phiên bản `1.28.0` (hiện chưa có tại thời điểm viết bài: đây chỉ là ví dụ). Nhớ thay thế tệp và liên kết [bằng phiên bản bạn muốn cài đặt] (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Ngoài ra, hãy tải xuống tệp chứa dấu vân tay và chữ ký PGP (một lần nữa, hãy nhớ điều chỉnh phiên bản trong lệnh):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Kiểm tra xem tệp dấu vân tay đã tải xuống đã được ký bằng khóa của nhà phát triển hay chưa:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Kết quả chính xác sẽ hiển thị:



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Cảnh báo khóa chưa được chứng thực có thể xuất hiện, nhưng điều này không quan trọng. Mặt khác, nếu chữ ký không hợp lệ hoặc tương ứng với một khóa khác, hãy dừng lại và bắt đầu lại, kiểm tra các liên kết.



Sau đó tính toán dấu vân tay SHA256 của kho lưu trữ và so sánh với tệp dấu vân tay chính thức:



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Nếu hai dấu vân tay trùng khớp hoàn toàn, kho lưu trữ là chính hãng và còn nguyên vẹn. Nếu chúng khác nhau, hãy xóa các tệp ngay lập tức và không tiếp tục.



Giải nén tệp lưu trữ trong thư mục gốc của bạn:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Sau đó sao chép nội dung vào thư mục Dojo, ghi đè lên nội dung cũ:



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Thao tác này giữ các tệp cấu hình của bạn nằm trong `~/dojo-app/docker/my-dojo/conf`, nhưng thay thế tất cả các tệp khác bằng phiên bản cập nhật.



Để giữ cho môi trường của bạn sạch sẽ, hãy xóa các tệp không cần thiết:



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Trở lại thư mục tập lệnh Dojo và chạy lệnh cập nhật:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Lệnh này hướng dẫn Docker xây dựng lại các ảnh với các tệp mới, sau đó tự động khởi động lại tất cả các dịch vụ. Khi kết thúc quá trình, hãy kiểm tra nhật ký để đảm bảo Bitcoin core, Fulcrum và Dojo đều hoạt động bình thường:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Nếu các dịch vụ khởi động mà không có lỗi và nhật ký hiển thị các khối đang được xử lý thì Dojo của bạn đã được cập nhật và hoạt động.