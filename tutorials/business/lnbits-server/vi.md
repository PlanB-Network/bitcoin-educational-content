---
name: Máy chủ LNbits
description: Cài đặt và cấu hình máy chủ LNbits tự lưu trữ trên Ubuntu VPS với PHOENIXD hoặc trên Umbrel
---

![cover](assets/cover.webp)



LNbits là ứng dụng web mã nguồn mở Interface, biến bất kỳ nền tảng Lightning nào (LND, Core Lightning, PHOENIXD) thành một nền tảng dịch vụ hoàn chỉnh. Giải pháp tự lưu trữ này cho phép bạn quản lý nhiều danh mục đầu tư Lightning một cách độc lập, triển khai điểm bán hàng, tạo hệ thống quyên góp hoặc dịch vụ thanh toán, đồng thời vẫn giữ được toàn quyền kiểm soát nguồn tiền của bạn.



Hướng dẫn này bao gồm hai phương pháp cài đặt: **VPS Ubuntu với PHOENIXD** (giải pháp gọn nhẹ không cần node Bitcoin đầy đủ) và **Umbrel** (tích hợp với node LND hiện có của bạn). Không giống như hướng dẫn LNbits chung của Plan B Network, bao gồm các khái niệm và tiện ích mở rộng, hướng dẫn này tập trung vào các quy trình cài đặt kỹ thuật từng bước.



## LNbits là gì?



LNbits là một hệ thống kế toán Lightning được phát triển bằng Python (FastAPI) kết nối với nền tảng hiện có (LND, Core Lightning, PHOENIXD). Không giống như các nút Lightning truyền thống, LNbits cung cấp Interface dễ tiếp cận, cho phép bạn quản lý nhiều danh mục đầu tư riêng biệt với khóa API riêng. Bạn có thể tạo tài khoản phụ cho gia đình, nhân viên hoặc dự án của mình mà không cần cấp quyền truy cập vào tất cả các khoản tiền của bạn.



Kiến trúc tách biệt lưu trữ thông tin trong SQLite (mặc định) hoặc PostgreSQL (sản xuất), trong khi nguồn lực vẫn được quản lý bởi nền tảng Lightning của bạn. Sự tách biệt này đảm bảo tính di động: bạn có thể di chuyển từ PHOENIXD sang LND mà không mất dữ liệu người dùng.



## Các tính năng chính



LNbits cung cấp một **hệ thống mở rộng** đa năng: TPoS (điểm bán hàng), Paywall (kiếm tiền từ nội dung), Sự kiện (bán vé), LndHub (máy chủ cho BlueWallet), Thẻ Bolt (thanh toán NFC), Thanh toán chia nhỏ (phân phối tự động) và Trình quản lý người dùng (quản lý người dùng bằng xác thực).



**Bảng điều khiển** hiển thị số dư theo thời gian thực, lịch sử giao dịch và các công cụ thanh toán. Mỗi Wallet có một URL duy nhất chứa khóa API, cho phép truy cập mà không cần đăng nhập truyền thống. Hệ thống khóa API ba cấp** (quản trị, Invoice, chỉ đọc) cung cấp khả năng kiểm soát chi tiết các quyền để tích hợp an toàn.



LNbits triển khai **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) và hỗ trợ **Lightning Address**, đảm bảo khả năng tương thích với ví Lightning hiện đại và tạo điều kiện triển khai các dịch vụ chuyên nghiệp.



## Nền tảng được hỗ trợ



**Ubuntu VPS**: Giải pháp nhẹ nhàng, không cần node Bitcoin đầy đủ. Yêu cầu: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. Cần có HTTPS + tên miền để hiển thị công khai (dịch vụ LNURL).



**Umbrel**: Dễ dàng cài đặt từ App Store. Điều kiện tiên quyết: nút Umbrel hoạt động với LND được đồng bộ hóa và các kênh mở. Cấu hình tự động.



Dưới đây là các liên kết đến hướng dẫn về Umbrel và Umbrel LND của chúng tôi:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Cài đặt trên Ubuntu VPS với PHOENIXD



### Bước 1: Bảo mật máy chủ VPS



**Trước khi cài đặt**, bạn cần bảo mật máy chủ VPS Ubuntu của mình theo các quy tắc hiện hành. Bước này **rất quan trọng** để bảo vệ cơ sở hạ tầng và tài khoản Lightning của bạn.



Sau đây là hướng dẫn chi tiết giúp bạn bắt đầu: **[Cấu hình máy chủ Ubuntu ban đầu - Hướng dẫn từng bước](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** của Daniel P. Costas.



Hướng dẫn này bao gồm cấu hình người dùng, SSH an toàn, tường lửa (UFW), fail2ban, cập nhật tự động và các biện pháp bảo mật hệ thống tốt.



### Bước 2: Cài đặt PHOENIXD



Sau khi máy chủ của bạn được bảo mật, bạn cần cài đặt và cấu hình PHOENIXD. Plan B Network cung cấp hướng dẫn chuyên sâu đầy đủ về cài đặt, tạo seed và cấu hình dịch vụ systemd:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Sau khi PHOENIXD được thiết lập và chạy (kiểm tra bằng `./Phoenix-CLI getinfo`), hãy ghi lại **mật khẩu HTTP** trong `~/.Phoenix/Phoenix.conf` - bạn sẽ cần mật khẩu này để kết nối LNbit với PHOENIXD.



### Triển khai LNbits



Cài đặt UV và sao chép LNbits:


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Cấu hình phần phụ trợ PHOENIXD:


```bash
cp .env.example .env && nano .env
```



Thêm vào `.env`:


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Kiểm tra bằng `uv run lnbits --host 0.0.0.0 --port 5000` sau đó tạo dịch vụ systemd với `Wants=PHOENIXD.service`.



## Thiết lập ban đầu và sử dụng lần đầu



### Kích hoạt SuperUser



Kích hoạt trình quản trị Interface trong `.env`:


```
LNBITS_ADMIN_UI=true
```



Khởi động lại LNbits (`sudo systemctl restart lnbits`) và lấy ID SuperUser:


```bash
cat ~/lnbits/data/.super_user
```



Truy cập `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` để vào bảng quản trị. Menu "Máy chủ" cho phép bạn cấu hình nguồn tài chính, tiện ích mở rộng và tài khoản người dùng.



### Tạo tài khoản an toàn



**Quan trọng khi công khai**: Nếu bạn đang công khai phiên bản LNbits của mình trên tên miền công cộng có thể truy cập được từ Internet, thì **điều quan trọng** là phải vô hiệu hóa tính năng tạo tài khoản người dùng miễn phí.



Từ trang quản trị SuperUser Interface, hãy vào "Cài đặt" rồi đến phần "Quản lý người dùng". Bạn sẽ thấy tùy chọn "Cho phép tạo người dùng mới".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Đối với triển lãm công cộng có tên miền**:




- Bạn phải tắt** tùy chọn "Cho phép tạo người dùng mới"
- Nếu không có sự bảo vệ này, bất kỳ ai trên Internet đều có thể tạo tài khoản trên phiên bản của bạn
- Kẻ tấn công có thể tạo tài khoản và sử dụng tính thanh khoản của LIGHTNING NODE của bạn mà bạn không biết
- Bạn sẽ cần tạo tài khoản người dùng theo cách thủ công từ Interface SuperUser



**Chỉ sử dụng tại địa phương** :




- Tùy chọn này ít quan trọng hơn nếu phiên bản của bạn chỉ có thể truy cập cục bộ (http://localhost:5000)
- Tuy nhiên, việc vô hiệu hóa tùy chọn này là một biện pháp an toàn chung tốt



Sau khi cấu hình, chỉ quản trị viên SuperUser mới có thể tạo tài khoản người dùng mới thông qua "Người dùng" Interface. Phương pháp này đảm bảo quyền kiểm soát hoàn toàn đối với những người có thể truy cập cơ sở hạ tầng Lightning và sử dụng tiền của bạn.



### Mở kênh đầu tiên



PHOENIXD tự động quản lý các kênh thông qua tính năng tự động thanh khoản. generate sử dụng Lightning Invoice với khoảng 30.000 Sats từ LNbit và thanh toán từ một Wallet khác. PHOENIXD tự động mở một kênh đến ACINQ. Phí mở kênh (khoảng 20-23.000 Sats) được khấu trừ, số dư còn lại (khoảng 7-10.000 Sats) sẽ xuất hiện sau khi On-Chain xác nhận.



Kiểm tra trạng thái bằng lệnh `./Phoenix-CLI getinfo`. Sau đó, hãy cân nhắc tắt tính năng tự động thanh khoản (`auto-liquidity=off` trong `Phoenix.conf`) để kiểm soát việc mở kênh.



### Hiển thị công khai và HTTPS



**Quan trọng**: Bắt buộc phải sử dụng HTTPS để hiển thị công khai (bảo mật khóa API + tương thích LNURL). Bỏ qua bước này nếu chỉ sử dụng cục bộ.



**Caddy (khuyến nghị)**: SSL tự động. `sudo apt install -y caddy`, chỉnh sửa `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Khởi động lại: `sudo systemctl restart caddy`.



**Nginx**: Kiểm soát nhiều hơn. Cài đặt `nginx certbot python3-certbot-nginx`, tạo `/etc/nginx/sites-available/lnbits`:


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Kích hoạt: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Thêm vào `.env`: `FORWARDED_ALLOW_IPS=*`



## Lắp đặt ô



### Triển khai từ App Store



Vào Umbrel App Store, tìm kiếm "LNbits" và nhấp vào "Cài đặt".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel tự động kiểm tra các phụ thuộc cần thiết. LNbits yêu cầu LIGHTNING NODE (LND) để chạy. Nếu LIGHTNING NODE của bạn đã hoạt động, hãy nhấp vào "Cài đặt LNbits" để xác nhận.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel tải xuống hình ảnh Docker, tự động cấu hình kết nối với LND và khởi động container (2-5 phút). Quá trình cài đặt diễn ra hoàn toàn ở chế độ nền.



### Cấu hình SuperUser ban đầu



Khi khởi chạy lần đầu, LNbits sẽ nhắc bạn tạo tài khoản quản trị viên SuperUser. Nhập tên người dùng và đặt mật khẩu an toàn để bảo vệ quyền truy cập vào hệ thống quản trị Interface.



![Configuration SuperUser](assets/fr/03.webp)



**Quan trọng**: Tài khoản SuperUser này có toàn quyền trên phiên bản LNbits của bạn. Hãy chọn mật khẩu mạnh và giữ an toàn.



Sau khi tạo tài khoản, bạn sẽ tự động được chuyển đến khu vực quản trị chính của Interface. Umbrel đã thiết lập LND làm nguồn tài trợ của bạn - tất cả các khoản thanh toán Lightning sẽ được thực hiện thông qua các kênh hiện có của bạn.



### Truy cập vào quản trị viên Interface



Trong menu bên trái, nhấp vào "Cài đặt" để truy cập toàn bộ bảng quản trị.



![Interface Settings](assets/fr/04.webp)



Phần "Quản lý ví" hiển thị thông tin chính về cấu hình của bạn:




- Nguồn tài trợ**: LndBtcRestWallet (kết nối trực tiếp đến nút LND Umbrel của bạn)
- Số dư nút**: Tổng thanh khoản có sẵn trong các kênh Lightning của bạn
- Số dư LNbits**: Số tiền được phân bổ cho hệ thống LNbits (ban đầu là 0 Sats)



Giờ đây, bạn có thể trực tiếp khai thác tính thanh khoản của nút Umbrel cho tất cả các ví LNbits mà bạn tạo. Không cần cấu hình bổ sung - LNbits đã sẵn sàng hoạt động.



### Quản lý người dùng



Một trong những tính năng mạnh mẽ nhất của LNbits là khả năng tạo nhiều người dùng độc lập, mỗi người dùng đều được xác thực bằng mật khẩu và có ví riêng biệt. Kiến trúc này cho phép bạn tận dụng tính thanh khoản của nút Umbrel, đồng thời cung cấp các tài khoản phụ hoàn toàn riêng biệt cho các mục đích sử dụng khác nhau: doanh nghiệp, gia đình, nhân viên, dự án, v.v.



Trong menu bên, nhấp vào "Người dùng" để truy cập quản lý người dùng. Nhấp vào "TẠO TÀI KHOẢN" để thêm người dùng mới.



![Gestion des utilisateurs](assets/fr/05.webp)



Điền vào mẫu tạo người dùng:




- Tên người dùng**: Tên người dùng đăng nhập (ví dụ: "Satoshi")
- Đặt mật khẩu**: Kích hoạt tùy chọn này để đặt mật khẩu xác thực
- Mật khẩu** và **Lặp lại mật khẩu**: Đặt mật khẩu cho người dùng này



![Création utilisateur satoshi](assets/fr/06.webp)



Các trường tùy chọn (Khóa công khai Nostr, Email, Tên, Họ) có thể để trống để tối thiểu hóa cấu hình. Nhấp vào "TẠO TÀI KHOẢN" để xác nhận.



![Confirmation utilisateur créé](assets/fr/07.webp)



Người dùng mới của bạn hiện sẽ xuất hiện trong danh sách người dùng với mã định danh và tên người dùng duy nhất.



![Liste des utilisateurs](assets/fr/08.webp)



**Điểm quan trọng**: Mỗi người dùng có thể đăng nhập hoàn toàn độc lập bằng mật khẩu riêng. Quản trị viên SuperUser giữ toàn quyền kiểm soát thông qua công cụ quản trị Interface.



### Quản lý người dùng Wallet



Bây giờ người dùng "Satoshi" đã được tạo, bạn cần gán cho người dùng đó một Wallet Lightning. Nhấp vào biểu tượng Wallet (biểu tượng thứ hai) của người dùng tương ứng, sau đó nhấp vào "TẠO Wallet MỚI".



![Gestion des wallets](assets/fr/09.webp)



Một hộp thoại sẽ nhắc bạn đặt tên cho Wallet. Nhập tên mô tả (ví dụ: "Wallet của Satoshi") và chọn loại tiền tệ hiển thị (CUC, USD, EUR, v.v.).



![Création wallet](assets/fr/10.webp)



Nhấp vào "TẠO". LNbits sẽ ngay lập tức tạo ra một Wallet Lightning đang hoạt động cho người dùng này.



![Confirmation wallet créé](assets/fr/11.webp)



Bây giờ bạn sẽ thấy hai ví hiện có: ví Wallet mặc định "LNbits Wallet" được tạo tự động và ví mới "Wallet Of Satoshi". Để đơn giản hóa trải nghiệm người dùng, bạn có thể xóa ví Wallet mặc định bằng cách nhấp vào biểu tượng xóa (thùng rác màu đỏ).



![Wallet final unique](assets/fr/12.webp)



Người dùng "Satoshi" hiện có một Wallet duy nhất, được xác định rõ ràng. Mỗi người dùng Wallet hoạt động hoàn toàn tự động, đồng thời sử dụng tính thanh khoản của nút LND cơ sở của bạn.



**Khái niệm chính**: Tất cả các ví này đều chia sẻ tính thanh khoản toàn cầu của nút Umbrel của bạn. Bạn không cần tạo kênh Lightning mới cho mỗi Wallet - LNbits hoạt động như một Layer kế toán thông minh, quản lý việc phân bổ vốn trong cơ sở hạ tầng Lightning hiện có của bạn. Đó chính là sức mạnh của hệ thống đa Wallet của LNbits.



### Đăng nhập người dùng



Đăng xuất khỏi tài khoản SuperUser (biểu tượng góc trên bên phải) và quay lại trang đăng nhập LNbits. Bây giờ bạn có thể đăng nhập bằng thông tin đăng nhập của người dùng mới.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Nhập tên người dùng ("Satoshi") và mật khẩu đã được thiết lập trước đó, sau đó nhấp vào "ĐĂNG NHẬP". Người dùng sẽ được truy cập trực tiếp vào tài khoản Wallet cá nhân của mình, hoàn toàn tách biệt với tài khoản quản trị Interface.



### Interface từ người dùng Wallet



Sau khi kết nối, người dùng có thể truy cập Interface từ Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Các tính năng của Interface:




- Số dư hiện tại**: Hiển thị theo Sats và theo loại tiền tệ đã chọn (CUC trong ví dụ này)
- Các hành động chính**: "DÁN YÊU CẦU" (dán hóa đơn để thanh toán), "TẠO Invoice" (generate biên lai), biểu tượng QR (quét nhanh)
- Lịch sử giao dịch**: Danh sách đầy đủ tất cả các khoản thanh toán và biên lai
- Bảng bên phải**: Tùy chọn cấu hình và truy cập



### Truy cập di động Wallet



Bảng điều khiển bên phải cung cấp một tính năng đặc biệt hữu ích: truy cập Wallet từ xa. Mở mục "Truy cập từ xa" để khám phá các tùy chọn khả dụng.



![Mobile Access](assets/fr/15.webp)



LNbits cung cấp một số cách để sử dụng Wallet này trên điện thoại thông minh:



**Tùy chọn 1: Ứng dụng di động tương thích




- Tải xuống **Zeus** hoặc **BlueWallet** từ App Store hoặc Google Play
- Kích hoạt phần mở rộng **LndHub** trong LNbits cho Wallet này
- Quét mã QR LndHub bằng ứng dụng di động để kết nối Wallet



**Tùy chọn 2: Truy cập trực tiếp qua trình duyệt di động**




- Mã QR hiển thị trong "Xuất sang điện thoại bằng mã QR" chứa URL đầy đủ của Wallet với xác thực tích hợp
- Quét mã QR này từ điện thoại thông minh của bạn để mở Wallet trực tiếp trong trình duyệt di động của bạn
- Thêm trang vào màn hình chính để truy cập nhanh



**Bảo mật quan trọng**: URL này chứa khóa API để truy cập đầy đủ vào Wallet. Tuyệt đối không chia sẻ công khai. Hãy coi mã QR này như khóa riêng tư Bitcoin của bạn - bất kỳ ai quét mã QR này đều có quyền truy cập đầy đủ vào Wallet.



Tính năng di động này biến phiên bản LNbits Umbrel của bạn thành một máy chủ Lightning Wallet thực sự dành cho bạn và bạn bè, đồng thời vẫn giữ được quyền quản lý hoàn toàn đối với tiền của bạn nhờ vào nút tự lưu trữ của bạn.



### Chia sẻ quyền truy cập của người dùng



Trường hợp sử dụng chính cho cấu hình nhiều người dùng này là **chia sẻ ví với gia đình hoặc nhóm bạn thân**. Sau khi tạo người dùng với mã Wallet chuyên dụng (chẳng hạn như "Satoshi" trong ví dụ của chúng tôi), bạn có thể chia sẻ thông tin đăng nhập này với các thành viên đáng tin cậy trong gia đình.



**Bảo mật truy cập trên Umbrel**: Quyền truy cập vào phiên bản LNbits của bạn trên Umbrel được bảo vệ tự nhiên vì chỉ có thể truy cập được:




- Trên mạng cục bộ của bạn**: Các thành viên trong gia đình bạn được kết nối với cùng mạng WiFi/Ethernet có thể truy cập vào phiên bản
- Qua VPN**: Nếu bạn sử dụng VPN như Tailscale được cấu hình trên máy chủ Umbrel của mình, người dùng được ủy quyền có thể truy cập từ xa an toàn



Cơ chế bảo vệ kép Layer (truy cập mạng + xác thực người dùng) này giúp tùy chọn "Cho phép tạo người dùng mới" ít quan trọng hơn trên Umbrel. Chỉ những người đã có quyền truy cập vào mạng hoặc VPN của bạn mới có thể đăng nhập bằng Interface.



**Tình huống điển hình**: Bạn tạo tài khoản "bố", tài khoản "mẹ", tài khoản "doanh nghiệp", v.v. Mỗi thành viên trong gia đình đều có một máy chủ Wallet Lightning riêng biệt, đồng thời được hưởng lợi từ tính thanh khoản chung của nút Umbrel. Chỉ cần chia sẻ tên người dùng và mật khẩu - sau đó người dùng có thể kết nối từ bất kỳ thiết bị nào trên mạng cục bộ hoặc thông qua VPN Tailscale của bạn. Vui lòng xem hướng dẫn Tailscale chuyên dụng của chúng tôi để biết thêm thông tin:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Khám phá các tiện ích mở rộng có sẵn



Quay lại Interface SuperUser và truy cập vào menu "Tiện ích mở rộng" ở bảng bên trái để khám phá toàn bộ hệ sinh thái tiện ích mở rộng LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits cung cấp danh mục tiện ích mở rộng phong phú giúp biến phiên bản của bạn thành nền tảng dịch vụ Lightning thực sự:





- Jukebox**: Hệ thống jukebox chạy bằng Sats (thanh toán bằng Spotify)
- Vé hỗ trợ**: Hệ thống hỗ trợ trả phí (nhận Satss để trả lời câu hỏi)
- TPoS**: Thiết bị đầu cuối điểm bán hàng di động an toàn dành cho các nhà bán lẻ
- Trình quản lý người dùng**: quản lý người dùng và Wallet nâng cao (mà chúng tôi vừa sử dụng)
- Sự kiện**: Bán và xác nhận vé sự kiện
- LNURLDevices**: Quản lý điểm bán hàng, ATM, thiết bị chuyển mạch được kết nối
- SMTP**: Cho phép người dùng gửi email và kiếm Satss
- Boltcards**: Lập trình thẻ NFC cho thanh toán chạm để thanh toán Lightning
- NostrNip5**: Tạo địa chỉ NIP5 cho tên miền của bạn
- Thanh toán chia nhỏ**: Tự động phân phối thanh toán giữa nhiều ví



Mỗi tiện ích mở rộng được kích hoạt chỉ bằng một cú nhấp chuột từ Interface này. Các tiện ích mở rộng được đánh dấu "MIỄN PHÍ" là miễn phí, trong khi một số có phiên bản "TRẢ PHÍ". Khám phá danh mục để tìm tiện ích phù hợp với nhu cầu của bạn - dù là cho doanh nghiệp, quản lý gia đình hay trải nghiệm các tính năng của Lightning Network.



## Ưu điểm và hạn chế



**Lợi ích**: Chủ quyền tài chính (kiểm soát hoàn toàn quỹ/khóa/dữ liệu), tính linh hoạt về kiến trúc (di chuyển VPS→Full node không mất dữ liệu), hệ thống mở rộng chuyên nghiệp, Interface trực quan.



**Hạn chế**: Phần mềm đang trong giai đoạn thử nghiệm (cần thận trọng về số lượng), bảo mật thuộc trách nhiệm của quản trị viên, URL chứa khóa API nhạy cảm (bắt buộc phải sử dụng HTTPS), quản lý nhiều người dùng đồng nghĩa với trách nhiệm giám sát.



## Thực hành tốt nhất



**Sao lưu**: seed PHOENIXD/credentials LND, cơ sở dữ liệu LNbits, tệp `.env`. Tự động hóa hàng ngày, không lưu trên máy chủ sản xuất, được mã hóa. Kiểm tra khôi phục thường xuyên.



**Bảo trì**: Thường xuyên kiểm tra các bản cập nhật (LNbits, Lightning backend, hệ điều hành). Luôn kiểm tra ghi chú phát hành trước khi có các bản cập nhật lớn.





- Trên Umbrel**: App Store sẽ tự động thông báo cho bạn về các phiên bản mới. Đồng bộ hóa tiện ích mở rộng qua "Quản lý Tiện ích mở rộng" > "Cập nhật Tất cả". Kiểm tra việc đưa cơ sở dữ liệu SQLite vào bản sao lưu tự động của Umbrel.
- Trên VPS**: Cập nhật thủ công bằng lệnh `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Theo dõi nhật ký hệ thống: `sudo journalctl -u lnbits -f`.



## Phần kết luận



Dịch vụ tự lưu trữ của LNbits mở ra một con đường cụ thể hướng đến chủ quyền tài chính Lightning. VPS+PHOENIXD cung cấp giải pháp gọn nhẹ cho các dịch vụ nhanh chóng, tích hợp hoàn toàn với node Bitcoin hiện có của Umbrel. Kiến trúc có khả năng mở rộng cho phép phát triển từ Wallet đa người dùng đơn giản sang các ứng dụng kinh doanh phức tạp.



Tự lưu trữ đồng nghĩa với trách nhiệm: sao lưu seed, bảo vệ quyền truy cập, bắt đầu với số lượng nhỏ. Với những biện pháp phòng ngừa này, LNbits trở thành một giải pháp mạnh mẽ cho nền kinh tế Lightning, đồng thời duy trì tính phi tập trung và tự chủ.



## Tài nguyên



### Tài liệu chính thức




- [Tài liệu LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Hướng dẫn cài đặt chính thức](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Hướng dẫn cộng đồng




- [Cấu hình máy chủ Ubuntu ban đầu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) của Daniel P. Costas (bảo mật VPS từng bước)
- [Cài đặt LNbits + PHOENIXD trên Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) của Daniel P. Costas (hướng dẫn đầy đủ)
- [Máy chủ LNbits trên Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) của Axel
- [LNbits trên VPS](https://github.com/TrezorHannes/vps-lnbits) của Hannes