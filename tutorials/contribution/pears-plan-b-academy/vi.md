---
name: Học viện Plan ₿ - Ứng dụng Pears
description: Làm thế nào để cài đặt và sử dụng ứng dụng Plan ₿ Academy trên Pears?
---

![cover](assets/cover.webp)


Có lẽ bạn đã biết rằng Plan₿ Academy là cơ sở dữ liệu giáo dục lớn nhất dành riêng cho Bitcoin, tập hợp các khóa học, hướng dẫn và hàng ngàn tài nguyên mã nguồn mở. Ban đầu, Plan₿ Academy là một trang web. Nhưng điều gì sẽ xảy ra nếu bạn không thể truy cập nó một cách bình thường nữa, chẳng hạn như trong trường hợp bị kiểm duyệt?


Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách vận hành nền tảng **Plan ₿ Academy** theo cách thực sự chống kiểm duyệt bằng cách sử dụng **Pears**, một công nghệ ngang hàng (P2P) do **Holepunch** phát triển và được **Tether** hỗ trợ.


Pears là phần mềm cho phép chúng ta vận hành nền tảng Plan₿ Academy mà không cần dựa vào một trang web tập trung. Trong hướng dẫn này, chúng tôi sẽ cài đặt Pears trên máy tính của bạn để truy cập Plan₿ Academy thông qua Pears.


Mục tiêu của Pears rất đơn giản: giúp việc phân phối và sử dụng các ứng dụng web trở nên khả thi mà không cần phụ thuộc vào bất kỳ cơ sở hạ tầng tập trung nào (không máy chủ, không máy chủ lưu trữ, không trung gian). Nói cách khác, ngay cả khi nhà cung cấp dịch vụ đám mây ngừng hoạt động hoặc một quốc gia chặn tên miền, ứng dụng vẫn tiếp tục tồn tại giữa các mạng ngang hàng. Cách tiếp cận này cho phép nền tảng giáo dục của chúng tôi, Plan ₿ Academy, duy trì khả năng truy cập trên toàn thế giới mà không gặp bất kỳ sự cố nào.


---

**Tóm tắt:**



- Cài đặt Pears;



- Chạy lệnh sau để khởi chạy ứng dụng Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Lê là gì?


Pears vừa là môi trường chạy, vừa là công cụ phát triển, vừa là nền tảng triển khai cho các ứng dụng ngang hàng. Công cụ mã nguồn mở này cho phép bạn xây dựng, chia sẻ và chạy phần mềm mà không cần máy chủ hay cơ sở hạ tầng, trực tiếp giữa người dùng. Về mặt thực tế, điều này có nghĩa là thay vì lưu trữ ứng dụng trên một máy chủ trung tâm, mỗi người dùng trở thành một nút trong mạng: họ chia sẻ một phần ứng dụng và dữ liệu với các nút khác. Toàn bộ hệ thống tạo thành một mạng lưới phân tán, trong đó mỗi phiên bản hợp tác để duy trì khả năng truy cập dịch vụ.


![Image](assets/fr/01.webp)


Phương pháp này dựa trên một tập hợp các thành phần phần mềm mô-đun được phát triển bởi Holepunch:



- Hypercore**: nhật ký phân tán đảm bảo tính nhất quán và bảo mật của dữ liệu mà không cần cơ sở dữ liệu trung tâm.
- Hyperbee**: một chỉ mục được xây dựng trên Hypercore cho phép tổ chức và truy vấn dữ liệu một cách hiệu quả.
- Hyperdrive**: một hệ thống tệp phân tán được sử dụng để lưu trữ và đồng bộ hóa các tệp ứng dụng giữa các đối tác.
- Hyperswarm** và **HyperDHT**: các lớp mạng cho phép khám phá và kết nối ngang hàng trên toàn thế giới mà không cần máy chủ trung tâm.
- Secretstream**: một giao thức mã hóa đầu cuối bảo mật thông tin liên lạc giữa các đối tác.


Bằng cách kết hợp các thành phần này, Pears cho phép tạo ra các ứng dụng tự chủ, được mã hóa và phân tán, nơi mọi người dùng đều tích cực tham gia vào mạng lưới. Kiến trúc phi tập trung này loại bỏ chi phí cơ sở hạ tầng, rủi ro kiểm duyệt và SPOF (*Điểm Lỗi Đơn*).


Pears được phát triển bởi Holepunch, một công ty do Mathias Buus và Paolo Ardoino (CEO của Tether và CTO của Bitfinex) sáng lập, với sứ mệnh mở rộng logic ngang hàng vượt ra ngoài Bitcoin. Tham vọng của họ là xây dựng “*Internet của các đồng nghiệp*”, nơi mọi ứng dụng có thể hoạt động mà không cần sự cho phép, không cần máy chủ và không cần trung gian. Holepunch hiện là đơn vị đứng sau **Keet**, một ứng dụng hội nghị truyền hình và nhắn tin hoàn toàn tương thích với P2P.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Hướng dẫn cài đặt Pears này được chia thành nhiều phần tùy thuộc vào hệ điều hành của bạn. Vui lòng truy cập trực tiếp vào phần tương ứng với môi trường của bạn để làm theo hướng dẫn phù hợp:*



- Linux (Debian)** → Phần **2**
- Windows** → Phần **3**
- macOS** → Phần **4**


## 2. Làm thế nào để cài đặt Pears trên Linux (Debian)?


Việc cài đặt Pears trên Debian tương đối đơn giản nhưng cần một số điều kiện tiên quyết mà chúng tôi sẽ trình bày chi tiết trong phần này.


### 2.1. Cập nhật hệ thống


Trước hết, điều quan trọng là phải đảm bảo hệ thống của bạn được cập nhật.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Cài đặt các phụ thuộc


Pears sử dụng một số thư viện hệ thống, bao gồm `libatomic1`, được sử dụng bởi công cụ chạy Bare JavaScript. Hãy cài đặt nó bằng lệnh sau:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Cài đặt Node.js và npm thông qua NVM


Pears được phân phối thông qua *npm*, trình quản lý gói *Node.js*. Mặc dù Pears không phụ thuộc trực tiếp vào *Node.js* để chạy, nhưng nó là bắt buộc để cài đặt. Cách được khuyến nghị để cài đặt *Node.js* trên Linux là thông qua *NVM* (*Trình quản lý Phiên bản Node*), cho phép bạn quản lý nhiều phiên bản Node song song.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Sau đó, tải lại thiết bị đầu cuối của bạn để kích hoạt *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Kiểm tra xem *NVM* đã được cài đặt đúng chưa:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Tiếp theo, hãy cài đặt phiên bản ổn định của *Node.js* (ví dụ: phiên bản LTS hiện tại):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Xác minh rằng *Node.js* và *npm* đã được cài đặt đúng cách:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Cài đặt Pears bằng npm


Khi *npm* khả dụng, bạn có thể cài đặt Pears CLI trên toàn hệ thống. Điều này cho phép bạn chạy lệnh `pear` từ bất kỳ thư mục nào.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Khởi tạo Pears


Sau khi cài đặt, chỉ cần chạy lệnh sau trong terminal của bạn:


```bash
pear
```


Khi khởi chạy lần đầu, Pears sẽ kết nối với mạng ngang hàng để tải xuống các thành phần cần thiết. Quá trình này không phụ thuộc vào bất kỳ máy chủ trung tâm nào — các tệp được lấy trực tiếp từ các máy ngang hàng khác.


![Image](assets/fr/10.webp)


Sau khi tải xuống hoàn tất, hãy chạy lại lệnh để xác nhận mọi thứ hoạt động:


```bash
pear
```


![Image](assets/fr/11.webp)


Nếu mọi thứ được cài đặt đúng cách, menu trợ giúp Pears sẽ xuất hiện với danh sách các lệnh có sẵn.


### 2.6. Thử nghiệm lê với Keet


Để xác minh Pears có hoạt động đầy đủ hay không, bạn có thể khởi chạy ứng dụng P2P hiện có trên mạng, chẳng hạn như Keet, phần mềm nhắn tin và hội nghị truyền hình nguồn mở do Holepunch phát triển.


```bash
pear run pear://keet
```


Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần sử dụng máy chủ trung tâm. Nếu Keet khởi chạy đúng cách, điều đó có nghĩa là cài đặt Pears của bạn đã hoạt động đầy đủ.


![Image](assets/fr/12.webp)


Hệ thống Linux của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng ngang hàng với Pears.


## 3. Cách cài đặt Pears trên Windows


Việc cài đặt Pears trên Windows cũng đơn giản như trên Linux nhưng cần một số công cụ cụ thể.


*Nếu bạn đang sử dụng Linux và đã cài đặt Pears, bạn có thể bỏ qua trực tiếp đến **Bước 5**.*


### 3.1. Mở PowerShell với tư cách Quản trị viên


Đầu tiên, hãy khởi chạy PowerShell với quyền quản trị viên:



- Nhấp vào menu Bắt đầu;
- Nhập “PowerShell”;
- Nhấp chuột phải vào "*Windows PowerShell*";
- Chọn "*Chạy với tư cách quản trị viên*".


![Image](assets/fr/15.webp)


### 3.2. Tải xuống NVS


Pears được cài đặt thông qua *npm*, trình quản lý gói *Node.js*. Trên Windows, phương pháp được Holepunch khuyến nghị là sử dụng *NVS* (*Node Version Switcher*), ổn định hơn *NVM* trên hệ thống này.


Trong PowerShell, hãy chạy lệnh sau để cài đặt phiên bản *NVS* mới nhất:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Cài đặt Node.js


Sau khi cài đặt, hãy khởi động lại PowerShell, sau đó nhập lệnh sau:


```powershell
nvs
```


Bạn sẽ thấy danh sách các phiên bản *Node.js* khả dụng. Chọn phiên bản đầu tiên bằng cách nhấn phím `a` trên bàn phím.


![Image](assets/fr/17.webp)


*Node.js* hiện đã được cài đặt.


![Image](assets/fr/18.webp)


### 3.4. Xác minh cài đặt


Đảm bảo *Node.js* và *npm* có thể truy cập được:


```powershell
node -v
npm -v
```


Cả hai lệnh đều phải trả về số phiên bản.


![Image](assets/fr/19.webp)


### 3.5. Cài đặt Pears bằng npm


Sau khi *Node.js* và *npm* đã sẵn sàng, hãy cài đặt **Pears CLI** trên toàn hệ thống của bạn:


```powershell
npm install -g pear
```


Thao tác này sẽ cài đặt tệp nhị phân `pear` vào thư mục *npm* toàn cục của bạn.


![Image](assets/fr/20.webp)


### 3.6. Xác minh và khởi tạo Pears


Sau khi cài đặt hoàn tất, hãy chạy:


```powershell
pear
```


Khi khởi chạy lần đầu, Pears sẽ tự động tải xuống các thành phần cần thiết từ mạng ngang hàng. Quá trình này có thể mất vài phút.


![Image](assets/fr/21.webp)


Nếu mọi việc diễn ra tốt đẹp, bạn sẽ thấy menu trợ giúp Pears CLI với danh sách các lệnh phụ có sẵn (chạy, seed, thông tin...).


### 3.7. Thử nghiệm lê với Keet


Để xác minh rằng Pears hoạt động hoàn toàn bình thường, bạn có thể khởi chạy ứng dụng P2P hiện có trên mạng, chẳng hạn như Keet — phần mềm nhắn tin và hội nghị truyền hình nguồn mở do Holepunch phát triển.


```bash
pear run pear://keet
```


Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần sử dụng bất kỳ máy chủ trung tâm nào. Nếu Keet khởi chạy thành công, điều đó có nghĩa là cài đặt Pears của bạn đã hoạt động đầy đủ.


![Image](assets/fr/22.webp)


Hệ thống Windows của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng ngang hàng với Pears.


## 4. Cách cài đặt Pears trên macOS


Việc cài đặt Pears trên macOS cũng tương tự như Linux nhưng cần một vài điều chỉnh riêng cho môi trường của Apple. Chúng ta hãy cùng xem qua các bước sau.


*Nếu bạn đang sử dụng Linux hoặc Windows và đã cài đặt Pears, bạn có thể bỏ qua trực tiếp đến **Bước 5**.*


### 4.1. Kiểm tra các điều kiện tiên quyết của hệ thống


Trước khi cài đặt, hãy đảm bảo *Xcode Command Line Tools* đã được cài đặt trên hệ thống của bạn. Gói này cung cấp các công cụ xây dựng cần thiết cho *Node.js* và các phần phụ thuộc của nó.


Để thực hiện việc này, hãy mở terminal bằng phím tắt `Cmd + Space bar`, nhập `Terminal` và nhấn `Enter`. Sau đó, chạy lệnh sau trong terminal để cài đặt:


```bash
xcode-select --install
```


Nếu các công cụ đã được cài đặt trên hệ thống của bạn, macOS sẽ thông báo cho bạn.


### 4.2. Cài đặt NVM


Pears được phân phối thông qua *npm*, trình quản lý gói *Node.js*. Mặc dù Pears không phụ thuộc trực tiếp vào *Node.js* để hoạt động, nhưng nó là bắt buộc để cài đặt. Phương pháp được khuyến nghị để cài đặt *Node.js* trên macOS là *NVM* (*Node Version Manager*), cho phép bạn quản lý nhiều phiên bản Node cùng lúc.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Sau đó tải lại thiết bị đầu cuối của bạn để kích hoạt *NVM*:


```bash
source ~/.zshrc
```


Nếu bạn sử dụng *bash* thay vì *zsh*, hãy chạy:


```bash
source ~/.bashrc
```


Tiếp theo, hãy kiểm tra xem *NVM* đã được cài đặt đúng chưa:


```bash
nvm --version
```


Thiết bị đầu cuối của bạn sẽ hiển thị phiên bản *NVM* đã cài đặt.


### 4.3. Cài đặt Node.js và npm


Tiếp theo, hãy cài đặt phiên bản ổn định của *Node.js* (ví dụ: phiên bản LTS hiện tại):


```bash
nvm install --lts
```


Sau khi cài đặt hoàn tất, hãy kiểm tra các phiên bản đã cài đặt:


```bash
node -v
npm -v
```


Cả hai lệnh đều phải trả về số phiên bản.


### 4.4. Cài đặt Pears bằng npm


Khi *npm* khả dụng, bạn có thể cài đặt Pears CLI trên toàn hệ thống. Điều này sẽ cho phép bạn thực thi lệnh `pear` từ bất kỳ thư mục nào.


```bash
npm install -g pear
```


### 4.5. Khởi tạo Pears


Sau khi cài đặt, chỉ cần chạy lệnh sau trong terminal của bạn:


```bash
pear
```


Khi khởi chạy lần đầu, Pears kết nối với mạng ngang hàng để tải xuống các thành phần cần thiết. Quá trình này không yêu cầu bất kỳ máy chủ trung tâm nào — các tệp được lấy trực tiếp từ các máy ngang hàng khác.


Sau khi tải xuống hoàn tất, hãy chạy lại lệnh để xác minh mọi thứ hoạt động:


```bash
pear
```


Nếu mọi thứ được cài đặt đúng cách, menu trợ giúp Pears sẽ xuất hiện với danh sách các lệnh có sẵn.


### 4.6. Thử nghiệm lê với Keet


Để xác minh Pears có hoạt động đầy đủ hay không, bạn có thể khởi chạy ứng dụng P2P đã có sẵn trên mạng, chẳng hạn như Keet, phần mềm nhắn tin và hội nghị truyền hình nguồn mở từ Holepunch.


```bash
pear run pear://keet
```


Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần sử dụng máy chủ trung tâm. Nếu Keet khởi chạy thành công, điều đó có nghĩa là cài đặt Pears của bạn đã hoạt động đầy đủ.


Hệ thống macOS của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng ngang hàng với Pears.


## 5. Cách sử dụng Plan ₿ Academy trên Pears


Sau khi Pears được cài đặt và chạy, bạn có thể khởi chạy trực tiếp nền tảng **Plan ₿ Academy** thông qua mạng P2P. Chỉ cần chạy lệnh sau trong terminal của bạn (lệnh này hoạt động trên Linux, Windows và macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Sau khi tải xong, Plan ₿ Academy sẽ mở trong môi trường Pears của bạn, sẵn sàng để sử dụng giống như trang web gốc — nhưng không phụ thuộc vào máy chủ trung tâm.


![Image](assets/fr/14.webp)


## 6. Cách gieo hạt giống cho kế hoạch ₿ Academy on Pears


Trong mạng Pears, *seed* một ứng dụng có nghĩa là phân phối lại ứng dụng đó cho các máy ngang hàng khác từ máy của bạn. Trên thực tế, khi bạn sử dụng seed Plan ₿ Academy, máy tính của bạn sẽ trở thành nguồn dữ liệu cho phép người dùng khác tải xuống ứng dụng mà không cần dựa vào máy chủ trung tâm.


Cơ chế này tăng cường khả năng phục hồi và khả năng chống kiểm duyệt của ứng dụng trên mạng Pears. Càng nhiều nút ngang hàng seed, ứng dụng càng trở nên khả dụng và phi tập trung, ngay cả khi một số nút gốc ngừng hoạt động.


Để giúp phân phối Plan ₿ Academy, chỉ cần chạy lệnh sau:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Miễn là lệnh này vẫn còn hiệu lực, thiết bị của bạn sẽ tham gia vào việc phân phối các tệp của ứng dụng. Nếu bạn đóng terminal, quá trình chia sẻ sẽ dừng lại.


Để tiếp tục gieo hạt sau khi khởi động lại, bạn có thể chạy lệnh ở chế độ nền hoặc tạo một dịch vụ hệ thống — ví dụ: dịch vụ systemd trên Linux, LaunchAgent trên macOS hoặc tác vụ theo lịch trình trên Windows. Các phương pháp này đảm bảo ứng dụng Plan₿ Academy tự động tiếp tục gieo hạt khi khởi động hệ thống.


Cảm ơn bạn đã đóng góp vào việc phân phối phi tập trung Plan ₿ Academy trên Pears và giúp cho nền giáo dục Bitcoin thực sự chống kiểm duyệt!