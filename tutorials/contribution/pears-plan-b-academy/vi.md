---
name: Plan ₿ Academy - Pears App
description: Làm thế nào để cài đặt và sử dụng ứng dụng Plan ₿ Academy trên Pears?
---

![cover](assets/cover.webp)

Có lẽ bạn đã biết, Plan ₿ Academy là cơ sở dữ liệu giáo dục lớn nhất dành riêng cho Bitcoin, bao gồm các khóa học, hướng dẫn và hàng ngàn tài nguyên được xuất bản dưới giấy phép mở (open-source). Ban đầu, Plan₿ Academy là một trang web. Nhưng điều gì sẽ xảy ra nếu bạn không thể truy cập nó một cách bình thường nữa, chẳng hạn như trong trường hợp bị kiểm duyệt?

Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách vận hành nền tảng **Plan ₿ Academy** theo cách chống kiểm duyệt bằng cách sử dụng **Pears**, một công nghệ ngang hàng (peer-to-peer, P2P) do **Holepunch** phát triển và được hỗ trợ bởi **Tether**.

Pears là phần mềm cho phép chúng ta vận hành nền tảng Plan ₿ Academy mà không cần dựa vào một trang web tập trung. Trong hướng dẫn này, chúng ta sẽ cài đặt Pears trên máy tính của bạn để truy cập Plan ₿ Academy thông qua Pears.

Mục tiêu của Pears rất đơn giản: cho phép phân phối và sử dụng các ứng dụng web mà không phụ thuộc vào bất kỳ hạ tầng tập trung nào (không máy chủ, không nhà cung cấp hosting, không trung gian). Nói cách khác, ngay cả khi một nhà cung cấp cloud ngừng hoạt động hoặc một quốc gia chặn một tên miền, ứng dụng vẫn tiếp tục hoạt động giữa các peer trong mạng. Chính cách tiếp cận này giúp nền tảng giáo dục Plan ₿ Academy luôn có thể truy cập ở mọi nơi trên thế giới, duy trì khả năng truy cập trên toàn thế giới mà không gặp bất kỳ sự cố nào.

---

**Tóm tắt nhanh:**

- Cài đặt Pears;

- Chạy lệnh sau để khởi động ứng dụng Plan ₿ Academy:

```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```

---

## 1. Pears là gì?

Pears vừa là môi trường thực thi (runtime environment), vừa là công cụ phát triển, và còn là nền tảng triển khai cho các ứng dụng P2P. Công cụ mã nguồn mở này cho phép bạn xây dựng, chia sẻ và chạy phần mềm mà không cần máy chủ hay cơ sở hạ tầng, thay vào đó là trực tiếp giữa các người dùng. Cụ thể, thay vì đặt ứng dụng trên một máy chủ trung tâm, mỗi người dùng sẽ trở thành một nút của mạng lưới, chia sẻ một phần ứng dụng và dữ liệu với các nút khác để duy trì khả năng truy cập của dịch vụ.

![Image](assets/fr/01.webp)

Phương pháp này dựa trên một tập hợp các thành phần phần mềm mô-đun được phát triển bởi Holepunch:

- **Hypercore**: một sổ cái phân tán đảm bảo tính nhất quán và an toàn của dữ liệu mà không cần cơ sở dữ liệu trung tâm.
- **Hyperbee**: lớp index nằm trên Hypercore, giúp tổ chức và truy vấn dữ liệu hiệu quả.
- **Hyperdrive**: hệ thống tệp phân tán dùng để lưu trữ và đồng bộ các tệp ứng dụng giữa các peer.
- **Hyperswarm** và **HyperDHT**: các lớp mạng cho phép các peer trên toàn cầu tìm thấy và kết nối với nhau mà không cần máy chủ trung tâm.
- **Secretstream**: một giao thức mã hóa đầu-cuối bảo giúp bảo mật các trao đổi giữa các peer.

Bằng cách kết hợp các thành phần này, Pears cho phép tạo ra các ứng dụng độc lập, được mã hóa và phân tán, nơi mỗi người dùng đều tham gia tích cực vào mạng. Kiến trúc phi tập trung này loại bỏ chi phí hạ tầng, rủi ro kiểm duyệt và các điểm lỗi duy nhất (SPOF - *Single Points of Failure*).

Pears được phát triển bởi Holepunch, một công ty do Mathias Buus và Paolo Ardoino (CEO của Tether và CTO của Bitfinex) sáng lập, với sứ mệnh mở rộng logic ngang hàng vượt ra ngoài Bitcoin. Tham vọng của họ là xây dựng “*Internet of peers*”, nơi mọi ứng dụng có thể hoạt động mà không cần sự cho phép, không máy chủ và không trung gian. Holepunch hiện là đơn vị đứng sau **Keet**, một ứng dụng nhắn tin và gọi video hoàn toàn tương thích với P2P.

https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Hướng dẫn cài đặt Pears này được chia thành nhiều phần tùy thuộc vào hệ điều hành của bạn. Hãy trực tiếp đi vào phần tương ứng với hệ điều hành của bạn để làm theo hướng dẫn:*

- **Linux (Debian)** → Phần **2**
- **Windows** → Phần **3**
- **macOS** → Phần **4**


## 2. Làm thế nào để cài đặt Pears trên Linux (Debian)?

Việc cài đặt Pears trên Debian tương đối đơn giản, nhưng cần một số bước chuẩn bị.

### 2.1. Cập nhật hệ thống

Trước tiên, hãy cập nhật hệ thống để đảm bảo mọi thứ đều ở phiên bản mới nhất.

```bash
sudo apt update && sudo apt upgrade -y
```

![Image](assets/fr/02.webp)

### 2.2. Cài đặt các dependencies (thư viện phụ thuộc)

Pears sử dụng một số thư viện hệ thống, bao gồm `libatomic1`, được sử dụng bởi Bare JavaScript runtime engine. Hãy cài đặt bằng lệnh sau:

```bash
sudo apt install -y libatomic1 curl git
```

![Image](assets/fr/03.webp)


### 2.3. Cài đặt Node.js và npm thông qua NVM

Pears được phân phối thông qua `npm`, trình quản lý gói *Node.js*. Mặc dù Pears không phụ thuộc trực tiếp vào *Node.js* để chạy, nhưng cần thiết cho quá trình cài đặt. Cách được khuyến nghị để cài đặt *Node.js* trên Linux là sử dụng *NVM* (*Node Version Manager*), cho phép bạn quản lý nhiều phiên bản Node song song.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

![Image](assets/fr/04.webp)

Sau đó, làm mới (reload) terminal của bạn để kích hoạt *NVM*:

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

Đảm bảo rằng *Node.js* và `npm` đã được cài đặt đúng cách:

```bash
node -v
npm -v
```

![Image](assets/fr/08.webp)

### 2.4. Cài đặt Pears bằng npm

Khi `npm` đã được cài, bạn có thể cài đặt Pears CLI trên toàn hệ thống (globally). Điều này cho phép bạn chạy lệnh `pear` từ bất kỳ thư mục nào.

```bash
npm install -g pear
```

![Image](assets/fr/09.webp)

### 2.5. Khởi tạo Pears

Sau khi cài đặt, chỉ cần chạy lệnh sau trong terminal:

```bash
pear
```

Khi khởi chạy lần đầu, Pears sẽ kết nối vào mạng peer-to-peer để tải xuống các thành phần cần thiết. Quá trình này không phụ thuộc vào bất kỳ máy chủ trung tâm nào — các tệp được lấy trực tiếp từ các peer khác.

![Image](assets/fr/10.webp)

Sau khi hoàn tất, hãy chạy lại lệnh để kiểm tra:

```bash
pear
```

![Image](assets/fr/11.webp)

Menu trợ giúp của Pears sẽ xuất hiện với danh sách các lệnh có sẵn.

### 2.6. Kiểm tra Pears với Keet

Để đảm bảo rằng Pears đang hoạt động đúng, bạn có thể khởi chạy một ứng dụng P2P hiện có trên mạng, chẳng hạn như Keet, phần mềm nhắn tin và gọi video mã nguồn mở do Holepunch phát triển.

```bash
pear run pear://keet
```

Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần thông qua máy chủ trung tâm. Nếu Keet khởi chạy thành công, điều đó có nghĩa là hệ thống Pears của bạn hoạt động tốt.

![Image](assets/fr/12.webp)

Hệ thống Linux của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng P2P với Pears.

## 3. Cách cài đặt Pears trên Windows

Việc cài đặt Pears trên Windows cũng đơn giản như trên Linux nhưng cần một số công cụ cụ thể.

*Nếu bạn đang sử dụng Linux và đã cài đặt Pears, bạn có thể bỏ qua trực tiếp đến **Bước 5**.*

### 3.1. Mở PowerShell với tư cách Quản trị viên

Đầu tiên, hãy khởi chạy PowerShell với quyền quản trị viên:

- Nhấp vào Start menu;
- Nhập “*PowerShell*”;
- Nhấp chuột phải vào "*Windows PowerShell*";
- Chọn "*Run as administrator*".

![Image](assets/fr/15.webp)

### 3.2. Tải xuống NVS

Pears được cài đặt thông qua `npm`, trình quản lý gói *Node.js*. Trên Windows, phương pháp được Holepunch khuyến nghị là sử dụng *NVS* (*Node Version Switcher*), ổn định hơn *NVM* trên hệ thống này.

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

*Node.js* giờ đây đã được cài đặt.

![Image](assets/fr/18.webp)

### 3.4. Xác minh cài đặt

Đảm bảo *Node.js* và `npm` có thể truy cập được:

```powershell
node -v
npm -v
```

Cả hai lệnh đều phải trả về số phiên bản của chúng.

![Image](assets/fr/19.webp)

### 3.5. Cài đặt Pears bằng npm

Sau khi *Node.js* và `npm` đã sẵn sàng, hãy cài đặt **Pears CLI** trên toàn hệ thống của bạn:

```powershell
npm install -g pear
```

Thao tác này sẽ cài đặt tệp nhị phân `pear` vào thư mục `npm` toàn cục của bạn.

![Image](assets/fr/20.webp)

### 3.6. Xác minh và khởi tạo Pears

Sau khi cài đặt hoàn tất, hãy chạy lệnh:

```powershell
pear
```

Khi khởi chạy lần đầu, Pears sẽ tự động tải xuống các thành phần cần thiết từ mạng peer-to-peer. Quá trình này có thể mất vài phút.

![Image](assets/fr/21.webp)

Bạn sẽ thấy menu trợ giúp Pears CLI với danh sách các lệnh phụ có sẵn (run, seed, info...).

### 3.7. Kiểm tra Pears với Keet

Để đảm bảo rằng Pears đang hoạt động đúng, bạn có thể khởi chạy một ứng dụng P2P hiện có trên mạng, chẳng hạn như Keet, phần mềm nhắn tin và gọi video mã nguồn mở do Holepunch phát triển.

```bash
pear run pear://keet
```

Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần thông qua máy chủ trung tâm. Nếu Keet khởi chạy thành công, điều đó có nghĩa là hệ thống Pears của bạn hoạt động tốt.

![Image](assets/fr/22.webp)


Hệ thống Windows của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng P2P với Pears.

## 4. Cài đặt Pears trên macOS

Việc cài đặt Pears trên macOS cũng tương tự như Linux nhưng cần một vài điều chỉnh riêng cho môi trường của Apple. Chúng ta hãy cùng xem qua các bước sau.

*Nếu bạn đang sử dụng Linux hoặc Windows và đã cài đặt Pears, bạn có thể bỏ qua và trực tiếp đến **Bước 5**.*


### 4.1. Kiểm tra hệ thống trước khi cài đặt

Trước khi cài đặt, hãy đảm bảo *Xcode Command Line Tools* đã được cài đặt trên hệ thống. Gói này cung cấp các công cụ build cần thiết cho *Node.js* và các dependencies.

Để thực hiện việc này, hãy mở terminal bằng phím tắt `Cmd + Phím cách`, nhập `Terminal` và nhấn `Enter`. Sau đó, chạy lệnh sau trong terminal để cài đặt:

```bash
xcode-select --install
```

Nếu *Xcode Command Line Tools* đã được cài đặt trên hệ thống, macOS sẽ thông báo cho bạn.

### 4.2. Cài đặt NVM

Pears được phân phối thông qua `npm`, trình quản lý gói *Node.js*. Mặc dù Pears không phụ thuộc trực tiếp vào *Node.js* để hoạt động, nhưng cần thiết cho quá trình cài đặt. Phương pháp được khuyến nghị để cài đặt *Node.js* trên macOS là *NVM* (*Node Version Manager*), cho phép bạn quản lý nhiều phiên bản Node cùng lúc.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

Sau đó, làm mới (reload) terminal của bạn để kích hoạt *NVM*:

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

Terminal của bạn sẽ hiển thị phiên bản *NVM* đã cài đặt.

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

Cả hai lệnh đều phải trả về số phiên bản của chúng.

### 4.4. Cài đặt Pears bằng npm

Khi `npm` đã được cài đặt, bạn có thể cài đặt Pears CLI trên toàn hệ thống. Việc này sẽ cho phép bạn thực thi lệnh `pear` từ bất kỳ thư mục nào.

```bash
npm install -g pear
```

### 4.5. Khởi tạo Pears

Sau khi cài đặt, chỉ cần chạy lệnh sau trong terminal:

```bash
pear
```

Khi khởi chạy lần đầu, Pears sẽ kết nối vào mạng peer-to-peer để tải xuống các thành phần cần thiết. Quá trình này không phụ thuộc vào bất kỳ máy chủ trung tâm nào — các tệp được lấy trực tiếp từ các peer khác.

Sau khi tải xuống hoàn tất, hãy chạy lại lệnh để kiểm tra:

```bash
pear
```

Menu trợ giúp Pears sẽ xuất hiện với danh sách các lệnh có sẵn.

### 4.6. Kiểm tra Pears với Keet

Để đảm bảo rằng Pears đang hoạt động đúng, bạn có thể khởi chạy một ứng dụng P2P hiện có trên mạng, chẳng hạn như Keet, phần mềm nhắn tin và gọi video mã nguồn mở do Holepunch phát triển.

```bash
pear run pear://keet
```

Lệnh này tải ứng dụng Keet trực tiếp từ mạng Pears mà không cần thông qua máy chủ trung tâm. Nếu Keet khởi chạy thành công, điều đó có nghĩa là hệ thống Pears của bạn hoạt động tốt.

Hệ thống macOS của bạn hiện đã sẵn sàng để chạy và lưu trữ các ứng dụng P2P với Pears.

## 5. Cách sử dụng Plan ₿ Academy trên Pears

Sau khi Pears được cài đặt và chạy, bạn có thể khởi chạy trực tiếp nền tảng **Plan ₿ Academy** thông qua mạng P2P. Chỉ cần chạy lệnh sau trong terminal của bạn (lệnh này hoạt động trên Linux, Windows và macOS):

```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```

![Image](assets/fr/13.webp)

Sau khi tải xong, Plan ₿ Academy sẽ mở trong môi trường Pears và hoạt động tương tự như trên website gốc, nhưng không phụ thuộc vào bất kỳ máy chủ tập trung nào.

![Image](assets/fr/14.webp)

## 6. Cách Seed Plan ₿ Academy on Pears

Trong mạng Pears, `seed` một ứng dụng có nghĩa là phân phối lại ứng dụng đó cho các peer khác từ chính máy của bạn. Khi bạn seed Plan ₿ Academy, máy tính của bạn trở thành một nguồn dữ liệu giúp người khác tải ứng dụng mà không cần máy chủ trung tâm.

Cơ chế này tăng cường khả năng chống kiểm duyệt và độ bền vững của ứng dụng trên mạng Pears. Càng nhiều peer seed, ứng dụng càng trở nên khả dụng và phi tập trung, ngay cả khi một số node gốc ngừng hoạt động.

Để giúp phân phối Plan ₿ Academy, chỉ cần chạy lệnh sau:

```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```

Trong suốt thời gian lệnh này chạy, thiết bị của bạn sẽ tham gia chia sẻ dữ liệu của ứng dụng. Khi bạn đóng terminal, quá trình seed sẽ dừng lại.

Để tiếp tục seed sau khi khởi động lại, bạn có thể chạy lệnh ở chế độ nền hoặc tạo một dịch vụ hệ thống — ví dụ: dịch vụ `systemd` trên Linux, LaunchAgent trên macOS hoặc tác vụ theo lịch trình trên Windows. Các phương pháp này đảm bảo ứng dụng Plan ₿ Academy tự động seed khi hệ thống khởi động.

Cảm ơn bạn đã đóng góp vào việc phân phối phi tập trung Plan ₿ Academy trên Pears và giúp cho nền giáo dục Bitcoin theo cách thực sự không thể kiểm duyệt!