---
name: Lê
description: Làm thế nào để cài đặt và sử dụng ứng dụng trên Pears?
---

![cover](assets/cover.webp)



Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách chạy ứng dụng trên **Pears**, một công nghệ ngang hàng (P2P) do **Holepunch** phát triển và được **Tether** hỗ trợ. Mục tiêu rất đơn giản: giúp phân phối và sử dụng các ứng dụng web mà không cần dựa vào bất kỳ cơ sở hạ tầng tập trung nào (không máy chủ, không host, không trung gian). Nói cách khác, ngay cả khi nhà cung cấp dịch vụ đám mây đóng cửa hoặc một quốc gia chặn tên miền, ứng dụng vẫn tồn tại giữa các mạng ngang hàng.



## 1. Lê là gì?



Pears là một môi trường thời gian chạy, công cụ phát triển và nền tảng triển khai cho các ứng dụng ngang hàng. Công cụ nguồn mở này cho phép xây dựng, chia sẻ và chạy phần mềm trực tiếp giữa người dùng mà không cần máy chủ hoặc cơ sở hạ tầng. Cụ thể, điều này có nghĩa là thay vì lưu trữ ứng dụng trên một máy chủ trung tâm, mỗi người dùng trở thành một nút mạng, chia sẻ một phần ứng dụng và dữ liệu với các nút ngang hàng khác. Toàn bộ hệ thống tạo thành một mạng lưới phân tán, trong đó mỗi phiên bản hợp tác để duy trì khả năng truy cập dịch vụ.



![Image](assets/fr/01.webp)



Phương pháp này dựa trên một bộ phần mềm mô-đun được phát triển bởi Holepunch:




- Hypercore**: nhật ký phân tán đảm bảo tính nhất quán và bảo mật của dữ liệu mà không cần cơ sở dữ liệu trung tâm.
- Hyperbee**: một công cụ lập chỉ mục trên Hypercore, giúp tổ chức và duyệt dữ liệu hiệu quả.
- Hyperdrive**: một hệ thống tệp phân tán được sử dụng để lưu trữ và đồng bộ hóa các tệp ứng dụng giữa các đối tác.
- Hyperswarm** và **HyperDHT**: các lớp mạng cho phép khám phá và kết nối giữa các đối tác trên toàn thế giới mà không cần máy chủ trung tâm.
- Secretstream**: một giao thức mã hóa E2E để bảo mật trao đổi giữa hai đối tác.



Bằng cách kết hợp các thành phần này, Pears cho phép tạo ra các ứng dụng tự chủ, được mã hóa và phân tán, trong đó mỗi người dùng đều tích cực tham gia vào mạng lưới. Kiến trúc phi tập trung này loại bỏ chi phí cơ sở hạ tầng, rủi ro kiểm duyệt và SPOF (*Điểm Lỗi Đơn*).



## 2. Nguồn gốc và triết lý của dự án



Pears đang được phát triển bởi Holepunch, một công ty do Mathias Buus và Paolo Ardoino (CEO của Tether và CTO của Bitfinex) sáng lập, với sứ mệnh mở rộng logic ngang hàng vượt ra ngoài Bitcoin. Tham vọng của họ là xây dựng "Internet ngang hàng", nơi mọi ứng dụng có thể chạy mà không cần ủy quyền, không cần máy chủ và không cần trung gian. Holepunch hiện là đơn vị đứng sau **Keet**, một ứng dụng hội nghị truyền hình và nhắn tin hoàn toàn theo chuẩn P2P.



*Hướng dẫn cài đặt Pears này được chia thành nhiều phần tùy thuộc vào hệ điều hành của bạn. Vui lòng truy cập trực tiếp vào phần tương ứng với môi trường của bạn để làm theo hướng dẫn phù hợp :*




- Linux (Debian)** → Phần **3**
- Windows** → Phần **4**
- macOS** → Phần **5**



## 3. Cách cài đặt Pears trên Linux (Debian)



Việc cài đặt Pears trên hệ thống Debian khá đơn giản, nhưng cần một số điều kiện tiên quyết mà chúng tôi sẽ trình bày chi tiết trong phần này.



### 3.1. cập nhật hệ thống



Đầu tiên và quan trọng nhất, điều quan trọng là phải đảm bảo hệ thống của bạn được cập nhật.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. cài đặt các phụ thuộc



Pears dựa trên một số thư viện hệ thống nhất định, đáng chú ý là `libatomic1`, được sử dụng bởi Bare JavaScript runtime. Hãy cài đặt nó bằng lệnh sau:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. Cài đặt Node.js và npm qua NVM



Pears được phân phối thông qua *npm*, trình quản lý gói *Node.js*. Mặc dù Pears không phụ thuộc trực tiếp vào *Node.js* để hoạt động, nhưng nó vẫn cần thiết cho việc cài đặt. Phương pháp được khuyến nghị để cài đặt *Node.js* trên Linux là *NVM* (*Node Version Manager*), cho phép bạn quản lý nhiều phiên bản Node song song.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Sau đó tải lại thiết bị đầu cuối của bạn để kích hoạt *NVM*:



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Kiểm tra xem *NVM* đã được cài đặt chưa:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Sau đó cài đặt phiên bản ổn định của *Node.js* (ví dụ: LTS hiện tại):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Kiểm tra cài đặt *Node.js* và *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Cài đặt Pears bằng npm



Khi *npm* khả dụng, bạn có thể cài đặt Pears CLI trên toàn hệ thống. Điều này sẽ cho phép bạn chạy lệnh `pear` từ bất kỳ thư mục nào.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Khởi tạo Pears



Sau khi cài đặt, chỉ cần chạy lệnh sau trong terminal của bạn:



```bash
pear
```



Khi khởi động lần đầu, Pears sẽ kết nối với mạng ngang hàng để tải xuống các thành phần cần thiết. Quá trình này không yêu cầu máy chủ trung tâm: các tệp được lấy trực tiếp từ các máy ngang hàng khác.



![Image](assets/fr/10.webp)



Sau khi tải xuống hoàn tất, hãy chạy lại lệnh để kiểm tra xem mọi thứ có hoạt động không:



```bash
pear
```



![Image](assets/fr/11.webp)



Nếu mọi thứ được cài đặt đúng cách, Pears Help sẽ hiển thị danh sách các lệnh có sẵn.



### 3.6. Kiểm tra lê với Keet



Để kiểm tra xem Pears có hoạt động đầy đủ hay không, bạn có thể khởi chạy ứng dụng P2P đã có sẵn trên mạng, chẳng hạn như Keet, phần mềm nhắn tin và hội nghị truyền hình nguồn mở của Holepunch.



```bash
pear run pear://keet
```



Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần thông qua máy chủ trung tâm. Nếu Keet khởi chạy đúng cách, cài đặt Pears của bạn sẽ hoạt động đầy đủ.



![Image](assets/fr/12.webp)



Hệ thống Linux của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng ngang hàng với Pears.



## 4. Cách cài đặt Pears trên Windows



Việc cài đặt Pears trên Windows cũng dễ như trên Linux, nhưng cần một số công cụ đặc biệt.



*Nếu bạn đang sử dụng Linux, bạn có thể bỏ qua bước 6.*



### 4.1. mở PowerShell ở chế độ quản trị viên



Trước hết, hãy chạy PowerShell với quyền quản trị viên:




- Nhấp vào menu Bắt đầu;
- Nhập PowerShell;
- Nhấp chuột phải vào "*Windows PowerShell*";
- Chọn "*Chạy với tư cách quản trị viên*".



![Image](assets/fr/15.webp)



### 4.2. Tải xuống NVS



Pears được cài đặt thông qua *npm*, trình quản lý gói *Node.js*. Trên Windows, phương pháp được Holepunch khuyến nghị là sử dụng *NVS* (*Node Version Switcher*), ổn định hơn *NVM* trên hệ thống này.



Trong PowerShell, hãy chạy lệnh sau để cài đặt phiên bản mới nhất của *NVS*:



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. cài đặt Node.js



Sau khi cài đặt, hãy khởi động lại PowerShell và nhập lệnh sau:



```powershell
nvs
```



Bạn sẽ thấy danh sách các phiên bản *Node.js* khả dụng. Chọn phiên bản đầu tiên bằng cách nhấn phím `a` trên bàn phím.



![Image](assets/fr/17.webp)



*Node.js* đã được cài đặt.



![Image](assets/fr/18.webp)



### 4.4. Kiểm tra cài đặt



Đảm bảo *Node.js* và *npm* có thể truy cập được:



```powershell
node -v
npm -v
```



Cả hai lệnh đều phải trả về số phiên bản.



![Image](assets/fr/19.webp)



### 4.5. Cài đặt Pears bằng npm



Sau khi *Node.js* và *npm* đã sẵn sàng, hãy cài đặt **Pears CLI** trên toàn hệ thống của bạn:



```powershell
npm install -g pear
```



Thao tác này sẽ cài đặt nhị phân `pear` vào thư mục *npm* toàn cục của bạn.



![Image](assets/fr/20.webp)



### 4.6. Kiểm tra và khởi tạo Pears



Sau khi cài đặt hoàn tất, hãy chạy:



```powershell
pear
```



Khi khởi chạy lần đầu, Pears sẽ tự động tải xuống các thành phần cần thiết từ mạng ngang hàng. Quá trình này có thể mất vài phút.



![Image](assets/fr/21.webp)



Nếu mọi việc diễn ra tốt đẹp, bạn sẽ thấy màn hình trợ giúp CLI Pears với danh sách các lệnh phụ có sẵn (chạy, seed, thông tin...).



### 4.7. Kiểm tra lê với Keet



Để kiểm tra xem Pears có hoạt động đầy đủ hay không, bạn có thể khởi chạy ứng dụng P2P đã có sẵn trên mạng, chẳng hạn như Keet, phần mềm nhắn tin và hội nghị truyền hình nguồn mở của Holepunch.



```bash
pear run pear://keet
```



Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần thông qua máy chủ trung tâm. Nếu Keet khởi chạy đúng cách, cài đặt Pears của bạn sẽ hoạt động đầy đủ.



![Image](assets/fr/22.webp)



Hệ thống Windows của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng ngang hàng với Pears.



## 5. Làm thế nào để cài đặt Pears trên macOS?



Việc cài đặt Pears trên macOS cũng tương tự như cài đặt trên Linux, nhưng cần một vài điều chỉnh riêng cho môi trường Apple. Hãy cùng khám phá các bước này.



*Nếu bạn đang sử dụng Linux hoặc Windows và đã cài đặt Pears, bạn có thể tiến hành trực tiếp đến **bước 6**.*



### 5.1. Kiểm tra yêu cầu hệ thống



Trước khi cài đặt, vui lòng đảm bảo *Xcode Command Line Tools* đã có trên hệ thống của bạn. Gói này cung cấp các công cụ biên dịch cần thiết cho _Node.js_ và các gói phụ thuộc của nó.



Để thực hiện việc này, hãy mở terminal bằng phím tắt `Cmd + Spacebar`, sau đó nhập `Terminal` và nhấn phím `Enter`. Sau đó, bạn có thể nhập lệnh này vào terminal để khởi chạy cài đặt:



```bash
xcode-select --install
```



Nếu các công cụ đã được cài đặt trên hệ thống của bạn, macOS sẽ thông báo cho bạn.



### 5.2. cài đặt NVM



Pears được phân phối thông qua *npm*, trình quản lý gói *Node.js*. Mặc dù Pears không phụ thuộc trực tiếp vào *Node.js* để hoạt động, nhưng nó vẫn cần thiết cho việc cài đặt. Phương pháp được khuyến nghị để cài đặt *Node.js* trên macOS là *NVM* (*Node Version Manager*), cho phép bạn quản lý nhiều phiên bản Node song song.



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



Sau đó kiểm tra xem *NVM* đã được cài đặt chưa:



```bash
nvm --version
```



Thiết bị đầu cuối sẽ trả về phiên bản *NVM* được cài đặt trên hệ thống của bạn.



### 5.3. Cài đặt Node.js và npm



Sau đó cài đặt phiên bản ổn định của *Node.js* (ví dụ: LTS hiện tại):



```bash
nvm install --lts
```



Sau khi cài đặt hoàn tất, hãy kiểm tra các phiên bản đã cài đặt:



```bash
node -v
npm -v
```



Cả hai lệnh đều phải trả về số phiên bản.



### 5.4 Cài đặt Pears bằng npm



Khi *npm* khả dụng, bạn có thể cài đặt Pears CLI trên toàn hệ thống. Điều này sẽ cho phép bạn chạy lệnh `pear` từ bất kỳ thư mục nào.



```bash
npm install -g pear
```



### 5.5. Khởi tạo Pears



Sau khi cài đặt, chỉ cần chạy lệnh sau trong terminal của bạn:



```bash
pear
```



Khi khởi động lần đầu, Pears sẽ kết nối với mạng ngang hàng để tải xuống các thành phần cần thiết. Quá trình này không yêu cầu máy chủ trung tâm: các tệp được lấy trực tiếp từ các máy ngang hàng khác.



Sau khi tải xuống hoàn tất, hãy chạy lại lệnh để kiểm tra xem mọi thứ có hoạt động không:



```bash
pear
```



Nếu mọi thứ được cài đặt đúng cách, Pears Help sẽ hiển thị danh sách các lệnh có sẵn.



### 5.6. Kiểm tra lê với Keet



Để kiểm tra xem Pears có hoạt động đầy đủ hay không, bạn có thể khởi chạy ứng dụng P2P đã có sẵn trên mạng, chẳng hạn như Keet, phần mềm nhắn tin và hội nghị truyền hình nguồn mở của Holepunch.



```bash
pear run pear://keet
```



Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần thông qua máy chủ trung tâm. Nếu Keet khởi chạy đúng cách, cài đặt Pears của bạn sẽ hoạt động đầy đủ.



Hệ thống macOS của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng ngang hàng với Pears.



## 6. Làm thế nào để sử dụng ứng dụng trên Pears?



Sau khi Pears được thiết lập và chạy, bạn có thể chạy ứng dụng bạn chọn trực tiếp bằng lệnh sau:



```bash
pear run pear://[KEY]
```



Chỉ cần thay thế `[KEY]` bằng khóa ứng dụng mà bạn muốn sử dụng.



![Image](assets/fr/13.webp)



Để tìm hiểu cách vận hành nền tảng Plan ₿ Academy của chúng tôi trên Pears, hãy xem hướng dẫn toàn diện này:



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Và để tìm hiểu cách sử dụng ứng dụng nhắn tin Keet mà bạn vừa ra mắt trên Pears, hãy xem hướng dẫn này:



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b