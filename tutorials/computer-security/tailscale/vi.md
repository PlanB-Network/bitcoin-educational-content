---
name: Vảy đuôi
description: Hướng dẫn nâng cao Tailscale
---
![cover](assets/cover.webp)



## 1. Giới thiệu



Tailscale là VPN thế hệ tiếp theo tạo ra mạng lưới được mã hóa giữa các thiết bị của bạn. Nó cho phép bạn kết nối các máy từ xa như thể chúng nằm trên cùng một mạng cục bộ, mà không cần cấu hình phức tạp hoặc mở cổng.



Đối với tự lưu trữ, Tailscale chỉ định cho mỗi thiết bị một IP riêng cố định trong mạng ảo, cung cấp quyền truy cập ổn định vào các dịch vụ của bạn ngay cả khi IP công cộng của bạn thay đổi. Điều này có nghĩa là bạn có thể quản lý máy chủ của mình từ xa mà không cần phải đưa các dịch vụ của mình trực tiếp ra Internet.



**Ứng dụng chính:**




- Quản lý máy chủ cá nhân từ bên ngoài
- Quản lý các nút Umbrel/Lightning nhanh hơn Tor
- Truy cập an toàn vào Raspberry Pi hoặc NAS
- Kết nối với các dịch vụ của bạn thông qua SSH hoặc HTTP mà không cần cấu hình mạng phức tạp



Cách tiếp cận tập trung vào sự đơn giản này cho phép những người tự lưu trữ truy cập vào dịch vụ của họ một cách an toàn, tránh được những cạm bẫy của VPN truyền thống.



## 2. Tailscale hoạt động như thế nào



Không giống như VPN truyền thống, định tuyến tất cả lưu lượng truy cập qua một máy chủ trung tâm, Tailscale tạo ra một mạng lưới nơi các thiết bị giao tiếp trực tiếp với nhau. Máy chủ trung tâm chỉ xử lý xác thực và phân phối khóa mà không xem dữ liệu người dùng.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Hình 1: VPN truyền thống với kiến trúc hub-and-spoke trong đó tất cả lưu lượng đều đi qua một máy chủ trung tâm*



Dựa trên WireGuard, mỗi thiết bị tạo ra các khóa mật mã riêng. Máy chủ điều phối phân phối các khóa công khai cho các nút, sau đó thiết lập các đường hầm được mã hóa đầu cuối trực tiếp giữa chúng. Để vượt qua tường lửa, Tailscale sử dụng NAT traversal và, như một phương sách cuối cùng, các rơle DERP duy trì mã hóa.



![VPN maillé (mesh)](assets/fr/02.webp)


*Hình 2: Mạng lưới Tailscale nơi các thiết bị giao tiếp trực tiếp với nhau*



Tất cả các thông tin liên lạc đều được mã hóa bằng WireGuard. Tailscale chỉ thấy siêu dữ liệu (kết nối) nhưng không bao giờ thấy nội dung trao đổi. Để có chủ quyền lớn hơn, Headscale cho phép máy chủ điều phối tự lưu trữ.



**Bảo mật và tính bảo mật:** Nhờ WireGuard, mọi giao tiếp trên Tailscale đều được mã hóa đầu cuối. Tailscale không thể đọc lưu lượng truy cập của bạn - chỉ các thiết bị của bạn mới có khóa riêng cần thiết. Dịch vụ chỉ thấy siêu dữ liệu: địa chỉ IP, tên thiết bị, dấu thời gian kết nối và nhật ký kết nối ngang hàng (không có nội dung).



Tuy nhiên, kiến trúc này phụ thuộc vào Tailscale Inc. để phối hợp mạng. Để loại bỏ sự phụ thuộc này, Headscale cung cấp một giải pháp thay thế nguồn mở cho phép bạn tự lưu trữ máy chủ điều khiển trong khi sử dụng các máy khách Tailscale chính thức, do đó đảm bảo chủ quyền hoàn toàn đối với cơ sở hạ tầng mạng của bạn, với chi phí cấu hình kỹ thuật hơn.



**Để biết giải thích chi tiết về hoạt động bên trong của Tailscale, bao gồm quản lý mặt phẳng điều khiển, chuyển tiếp NAT và DERP, chúng tôi khuyên bạn nên đọc bài viết tuyệt vời [Cách Tailscale hoạt động](https://tailscale.com/blog/how-tailscale-works) trên blog chính thức. Bài viết này giải thích sâu sắc các khái niệm kỹ thuật khiến Tailscale trở nên mạnh mẽ như vậy.



## 3. Cài đặt Tailscale



Tailscale chạy trên **hầu hết các hệ điều hành** phổ biến (Windows, macOS, Linux, iOS, Android). Việc cài đặt được cho là "nhanh chóng và dễ dàng" trên mọi nền tảng. Chúng ta hãy bắt đầu bằng cách xem Interface và cách tạo tài khoản, sau đó chuyển sang các quy trình cài đặt cho các môi trường khác nhau.



### 3.1 Tạo tài khoản Tailscale



Truy cập [https://tailscale.com/](https://tailscale.com/) và nhấp vào nút "Bắt đầu" ở góc trên bên phải của trang.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Trang chủ Tailscale giải thích khái niệm và cung cấp bản dùng thử miễn phí*



Để sử dụng Tailscale, trước tiên bạn cần tạo một tài khoản thông qua nhà cung cấp danh tính:



![Page de connexion Tailscale](assets/fr/04.webp)


*Lựa chọn nhà cung cấp danh tính để kết nối với Tailscale (Google, Microsoft, GitHub, Apple, v.v.)*



Sau khi đăng nhập, Tailscale sẽ yêu cầu bạn cung cấp một số thông tin về mục đích sử dụng của bạn:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Biểu mẫu để hiểu rõ hơn về trường hợp sử dụng của bạn (cá nhân hoặc chuyên nghiệp)*



Sau khi tạo tài khoản, bạn có thể cài đặt Tailscale trên thiết bị của mình:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale cho phép bạn cài đặt ứng dụng trên nhiều hệ thống khác nhau*



### 3.2 Cài đặt trên các nền tảng khác nhau





- Trên Windows và macOS:** Chỉ cần tải xuống ứng dụng đồ họa từ trang web chính thức của Tailscale và cài đặt (tệp .msi trên Windows, tệp .dmg trên Mac). Sau khi cài đặt, ứng dụng sẽ khởi chạy Interface đồ họa cho phép bạn kết nối (thông qua trình duyệt) với tài khoản Tailscale của mình để xác thực máy.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Kết nối MacBook với lưới đuôi*



![Connexion réussie](assets/fr/09.webp)


*Xác nhận thiết bị đã được kết nối với mạng Tailscale*





- Trên Linux (Debian, Ubuntu, v.v.):** Bạn có một số tùy chọn. Phương pháp đơn giản nhất là chạy tập lệnh cài đặt chính thức: ví dụ, trên Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Tập lệnh này sẽ thêm kho lưu trữ Tailscale chính thức và cài đặt gói. Bạn cũng có thể [thêm thủ công kho lưu trữ APT](https://pkgs.tailscale.com) hoặc sử dụng các gói Snap hoặc apt thông thường. Sau khi cài đặt, daemon `tailscaled` sẽ chạy ở chế độ nền. Sau đó, bạn sẽ cần **xác thực nút** (xem Interface CLI so với web bên dưới). Trên các bản phân phối khác (Fedora, Arch...), gói cũng có sẵn thông qua các kho lưu trữ chuẩn hoặc tập lệnh cài đặt chung. Đối với máy chủ không có giao diện, hãy sử dụng CLI: ví dụ `sudo tailscale up --auth-key <key>` nếu sử dụng khóa xác thực được tạo trước hoặc chỉ cần `tailscale up` để đăng nhập tương tác (sẽ cung cấp URL để truy cập để xác thực thiết bị).





- Trên các hệ thống dựa trên ARM (Raspberry Pi, v.v.):** Chúng tôi thường sử dụng Linux, do đó, cách tiếp cận tương tự như trên (script hoặc package). Lưu ý rằng Tailscale hỗ trợ kiến trúc ARM32/ARM64 mà không có bất kỳ vấn đề nào. Nhiều người dùng cài đặt Tailscale trên Raspberry Pi OS thông qua apt hoặc trên các bản phân phối nhẹ (DietPi, v.v.) để truy cập Pi của họ ở mọi nơi.





- Trên iOS và Android:** Tailscale cung cấp các ứng dụng di động **chính thức**. Chỉ cần cài đặt *Tailscale* từ [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) hoặc [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Các bước cài đặt Tailscale trên iPhone: chào mừng, quyền riêng tư, thông báo, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Kết nối với tailnet, chọn tài khoản và xác thực trên iPhone*



Sau khi ứng dụng được cài đặt, khi khởi chạy lần đầu, ứng dụng sẽ yêu cầu bạn xác thực thông qua nhà cung cấp đã chọn (Google, Apple ID, Microsoft, v.v., tùy thuộc vào những gì bạn đang sử dụng cho Tailscale) - đây là quy trình tương tự như trên các nền tảng khác, thường là chuyển hướng đến trang web OAuth. Sau đó, ứng dụng di động sẽ tạo VPN (trên iOS, bạn sẽ cần chấp nhận tiện ích bổ sung cấu hình VPN). Sau đó, ứng dụng có thể chạy ở chế độ nền, cho phép bạn truy cập vào tailnet của mình từ mọi nơi. *Xin lưu ý:* trên thiết bị di động, bạn chỉ có thể có **một VPN đang hoạt động tại một thời điểm** - vì vậy hãy đảm bảo rằng bạn không kết nối VPN khác cùng lúc, nếu không Tailscale sẽ không thể thiết lập VPN của riêng mình. Trên Android, bạn có thể thiết lập hồ sơ công việc riêng nếu muốn cô lập một số mục đích sử dụng nhất định (ví dụ: hồ sơ có Tailscale đang hoạt động cho một ứng dụng nhất định).



### 3.3 Thêm nhiều thiết bị và xác thực



Khi thiết bị đầu tiên của bạn được kết nối, Tailscale sẽ nhắc bạn thêm các thiết bị khác vào mạng của mình:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface hiển thị thiết bị đầu tiên được kết nối và đang chờ các thiết bị khác*



Sau khi đã thêm nhiều thiết bị, bạn có thể kiểm tra xem chúng có thể giao tiếp với nhau hay không:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Xác nhận các thiết bị có thể giao tiếp với nhau qua ping*



Sau đó Tailscale gợi ý các cấu hình bổ sung để nâng cao trải nghiệm của bạn:



![Suggestions de configuration](assets/fr/14.webp)


*Gợi ý về việc thiết lập DNS, chia sẻ thiết bị và quản lý quyền truy cập*



### 3.4 Bảng điều khiển quản trị



Bảng điều khiển quản trị web cho phép bạn xem và quản lý tất cả các thiết bị được kết nối của mình:



![Tableau de bord des machines](assets/fr/15.webp)


*Danh sách các thiết bị được kết nối cùng đặc điểm và trạng thái của chúng*



**Interface Web so với Interface CLI:** Tailscale cung cấp hai cách bổ sung cho nhau để tương tác với mạng: **quản trị web Interface** và **trình khách dòng lệnh (CLI)**.





- Interface Web (Bảng điều khiển dành cho quản trị viên)**: có thể truy cập tại [https://login.tailscale.com](https://login.tailscale.com), bảng điều khiển web này là bảng điều khiển trung tâm cho mạng Tailscale của bạn. Nó liệt kê tất cả các thiết bị (*Máy*), trạng thái trực tuyến/ngoại tuyến của chúng, địa chỉ IP Tailscale của chúng, v.v. Tại đây, bạn có thể **quản lý thiết bị** (đổi tên, hết hạn khóa, ủy quyền tuyến đường, vô hiệu hóa một nút), **quản lý người dùng** (trong bối cảnh tổ chức) và xác định các quy tắc bảo mật (ACL). Đây cũng là nơi bạn định cấu hình các tùy chọn toàn cầu như MagicDNS, thẻ hoặc khóa xác thực (khóa xác thực trước generate để tự động thêm thiết bị). Web Interface rất tiện dụng để có được cái nhìn tổng quan và áp dụng các thay đổi sẽ được truyền qua máy chủ phối hợp đến tất cả các nút. *Ví dụ:* Việc kích hoạt **tuyến đường mạng con** hoặc **nút thoát** được thực hiện chỉ bằng một cú nhấp chuột trong bảng điều khiển, sau khi nút đang đề cập đã tự thông báo như vậy.





- Dòng lệnh Interface (CLI):** Lệnh `tailscale` có sẵn trong CLI trên mọi thiết bị cài đặt Tailscale. CLI này cho phép bạn thực hiện mọi thứ cục bộ: kết nối (`tailscale up`), kiểm tra trạng thái (`tailscale status` để xem những đối tác nào đang kết nối), gỡ lỗi (`tailscale ping <ip>`), v.v. Một số tính năng thậm chí **chỉ có ở CLI** hoặc nâng cao hơn, ví dụ:





  - `tailscale up --advertise-routes=192.168.0.0/24` để quảng cáo một tuyến mạng con,
  - `tailscale up --advertise-exit-node` để đề xuất máy của bạn làm nút thoát,
  - `tailscale set --accept-routes=true` (hoặc `--exit-node=<IP>`) để sử dụng một tuyến đường hoặc một nút thoát,
  - `tailscale ip -4` để hiển thị IP Tailscale của thiết bị,
  - `khóa/mở khóa tailscale` (nếu sử dụng *tailnet-lock*, tính năng bảo mật nâng cao),
  - hoặc `tailscale file send <node>` để sử dụng **Taildrop** (truyền tệp giữa các thiết bị).


CLI rất hữu ích trên các máy chủ không có đồ họa Interface và để viết kịch bản cho một số hành động nhất định. **Sự khác biệt khi sử dụng:** Hầu hết các cấu hình cơ bản có thể được thực hiện thông qua Web hoặc qua CLI. Ví dụ, việc thêm thiết bị được thực hiện bằng cách nhắc qua bảng điều khiển hoặc bằng cách chạy `tailscale up` trên thiết bị và xác thực qua web. Tương tự như vậy, việc đổi tên thiết bị có thể được thực hiện thông qua bảng điều khiển hoặc bằng `tailscale set --hostname`. **Tóm lại**, bảng điều khiển web lý tưởng cho việc quản trị mạng toàn cầu (đặc biệt là với nhiều máy/người dùng), trong khi CLI tiện dụng để kiểm soát chi tiết một máy nhất định, các tập lệnh tự động hóa hoặc sử dụng trên hệ thống không có GUI.



## 4. Sử dụng Tailscale trên Umbrel



Umbrel là một nền tảng tự lưu trữ phổ biến (đặc biệt được sử dụng cho các nút Bitcoin/Lightning và các dịch vụ tự lưu trữ khác, thông qua App Store). Để cài đặt và cấu hình Umbrel, chúng tôi khuyên bạn nên làm theo hướng dẫn chuyên dụng của chúng tôi:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Sử dụng Umbrel và Tailscale cùng nhau là một trường hợp sử dụng đặc biệt thú vị, vì Umbrel tích hợp sẵn một mô-đun Tailscale dễ triển khai. Sau đây là cách Tailscale tích hợp với Umbrel và những gì nó mang lại:



### 4.1 Cài đặt và cấu hình ô





- Cài đặt Tailscale trên Umbrel:** Umbrel có ứng dụng Tailscale chính thức trên App Store. Việc cài đặt không thể đơn giản hơn:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Trang ứng dụng Tailscale trong Umbrel App Store*



Từ Interface Web Umbrel, mở App Store, tìm kiếm **Tailscale** và nhấp vào *Cài đặt*. Vài giây sau, ứng dụng được cài đặt trên Umbrel. Khi bạn mở ứng dụng, Umbrel sẽ hiển thị một trang cho phép bạn liên kết nút của mình với Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Màn hình kết nối Tailscale trong Interface của Umbrel*



Chỉ cần **nhấp vào "Đăng nhập"**, bạn sẽ được chuyển hướng đến trang xác thực Tailscale:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Kết nối với Tailscale thông qua nhà cung cấp danh tính*



Bạn có thể xác thực thông qua tài khoản Tailscale của mình (Google/GitHub/v.v.) hoặc nhập email của bạn. Thông thường, trên Umbrel, Interface yêu cầu bạn truy cập [https://login.tailscale.com](https://login.tailscale.com) và đăng nhập - điều này xác thực ứng dụng Umbrel Tailscale.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Xác nhận thiết bị Umbrel đã được kết nối với mạng Tailscale*



Sau khi hoàn tất, Umbrel của bạn sẽ "nằm trong" mạng Tailscale của bạn và xuất hiện trên bảng điều khiển với tên (ví dụ: *umbrel*). Sau đó, bạn có thể nhấp vào IP Address của thiết bị để sao chép, lấy IPv6 Address hoặc MagicDNS của bạn được liên kết với thiết bị của bạn.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Bảng điều khiển quản trị Tailscale hiển thị một số thiết bị được kết nối, bao gồm Umbrel*




### 4.2 Truy cập từ xa vào dịch vụ Umbrel



Sau khi Umbrel được kết nối với Tailscale, **bạn có thể truy cập Interface Umbrel và các ứng dụng đang chạy trên đó, từ bất kỳ đâu, như thể bạn đang ở trên mạng cục bộ**. Đây là một trong những lợi thế chính so với Tor.



Truy cập cực kỳ đơn giản: thay vì sử dụng `umbrel.local` (chỉ hoạt động trên mạng cục bộ của bạn), bạn sử dụng Umbrel's Tailscale IP Address (`http://100.x.y.z`) trực tiếp từ bất kỳ thiết bị nào được kết nối với tailnet của bạn. Điều này hoạt động bất kể bạn ở đâu hoặc sử dụng kết nối internet nào (4G, Wi-Fi công cộng, mạng công ty).



**Ví dụ về các ứng dụng được lưu trữ trên Umbrel có thể truy cập thông qua Tailscale:**





- Interface main Umbrel**: Truy cập bảng điều khiển Umbrel của bạn chỉ bằng cách nhập `http://100.x.y.z` vào trình duyệt của bạn
- Nút Bitcoin**: Quản lý nút Bitcoin của bạn mà không có độ trễ, xem đồng bộ hóa và thống kê
- Lightning Node**: Sử dụng ThunderHub, RTL hoặc các giao diện quản lý Lightning khác với khả năng phản hồi ngay lập tức
- Mempool**: Xem các giao dịch Bitcoin và Mempool mà không cần sự chậm trễ của Tor
- noStrudel**: Truy cập các dịch vụ Nostr của bạn được lưu trữ trên Umbrel



**Kết nối ví ngoài với nút Bitcoin hoặc nút Lightning của bạn thông qua Tailscale:**



Tailscale cũng cho phép ví Bitcoin và Lightning của bạn được cài đặt trên các thiết bị khác kết nối trực tiếp với nút Umbrel của bạn:





- Sparrow wallet (Bitcoin)**: Wallet Bitcoin bên ngoài này có thể kết nối trực tiếp với máy chủ Electrum của Umbrel bằng cách sử dụng Tailscale IP Address:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Cấu hình máy chủ Electrum riêng trong Sparrow wallet bằng cách sử dụng Tailscale IP Address của Umbrel*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Danh sách các bí danh máy chủ Electrum trong Sparrow có Umbrel Tailscale IP Address*



Đọc hướng dẫn đầy đủ của chúng tôi về cách cấu hình Sparrow wallet với nút Bitcoin của bạn:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Lightning)**: Wallet di động Lightning này có thể kết nối với nút Lightning của bạn trên Umbrel. Thay vì cấu hình điểm cuối là `.onion', chỉ cần đặt IP Tailscale của Umbrel và cổng Lightning API. Kết nối sẽ diễn ra ngay lập tức so với Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Cấu hình Zeus để kết nối với nút Lightning thông qua Tailscale* IP Address



Để cấu hình Zeus với nút Lightning của bạn, hãy xem hướng dẫn chi tiết của chúng tôi:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Để tìm hiểu thêm về Lightning Network và cách thức hoạt động của nó trên Umbrel, hãy truy cập:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Ưu điểm so với Tor



Umbrel cung cấp quyền truy cập từ xa thông qua Tor (bằng cách cung cấp địa chỉ `.onion` cho các dịch vụ web của mình). Trong khi Tor có lợi thế về tính bảo mật (ẩn danh) và không yêu cầu đăng ký, nhiều người dùng thấy **Tor chậm và không ổn định** khi sử dụng hàng ngày (các trang tải chậm, hết thời gian chờ, v.v.) - *"Umbrel qua Tor rất chậm "* một số người phàn nàn.



Tailscale cung cấp kết nối **nhanh hơn, độ trễ thấp** nói chung, vì lưu lượng đi qua trực tiếp (hoặc qua một rơle nhanh) thay vì phải chuyển qua 3 nút Tor. Hơn nữa, Tailscale cung cấp trải nghiệm "mạng cục bộ": sử dụng IP riêng và các ứng dụng có thể được ánh xạ trực tiếp (ví dụ: ổ đĩa mạng SMB trên \100.x.y.z).



Nói như vậy, Tor có lợi thế là phi tập trung và "sẵn sàng sử dụng" trên Umbrel, trong khi Tailscale liên quan đến việc tin tưởng một bên thứ ba (hoặc lưu trữ headscale). Tor cũng hữu ích cho việc truy cập không cần máy khách (từ bất kỳ trình duyệt Tor nào, bạn có thể tham khảo Giao diện người dùng Umbrel, trong khi Tailscale yêu cầu máy khách được cài đặt trên thiết bị truy cập).



**Tóm lại**, đối với mục đích sử dụng tương tác (ví Lightning, giao diện web thường xuyên), Tailscale cung cấp sự thoải mái và tốc độ đáng kể so với Tor, với cái giá là phụ thuộc bên ngoài một chút. Nhiều người chọn sử dụng *cả hai*: Tailscale hàng ngày và Tor như một giải pháp dự phòng hoặc chia sẻ quyền truy cập với ai đó mà không mời họ vào VPN của họ.



### 4.4 An toàn



Bằng cách sử dụng Tailscale với Umbrel, bạn tránh được việc Umbrel bị lộ ra Internet. Nút Umbrel chỉ có thể truy cập được bởi các thiết bị đã xác thực khác của bạn trong tailnet, giúp giảm đáng kể bề mặt tấn công (không có cổng nào mở cho người lạ, không có nguy cơ bị tấn công vào dịch vụ web qua Internet).



Truyền thông được mã hóa (WireGuard) ngoài bất kỳ mã hóa nào mà dịch vụ của bạn đang thực hiện (ví dụ: ngay cả HTTP nội bộ cũng nằm trong đường hầm). Bạn vẫn có thể áp dụng Tailscale ACL để, ví dụ, ngăn một thiết bị tailnet cụ thể truy cập Umbrel nếu bạn muốn phân vùng mạng. Bản thân Umbrel không thấy sự khác biệt - nó nghĩ rằng nó đang phục vụ cục bộ.



---

Để kết thúc phần này, tích hợp Tailscale trên Umbrel chỉ mất vài cú nhấp chuột và **cải thiện đáng kể khả năng truy cập** của nút tự lưu trữ của bạn. Bạn sẽ có thể quản lý Umbrel và các dịch vụ của nó từ bất kỳ đâu, an toàn và hiệu quả, giống như khi bạn ở nhà. Đây là giải pháp đặc biệt hữu ích cho các ứng dụng thời gian thực (Lightning) gặp phải độ trễ Tor hoặc nói chung là cho bất kỳ máy chủ tự lưu trữ nào đang tìm kiếm kết nối riêng tư đơn giản. Tất cả mà không cần để lộ một cổng nào** trên hộp của bạn và không cần cấu hình mạng phức tạp.



## 5. Quản lý nâng cao và các trường hợp sử dụng



### 5.1 Các tính năng nâng cao của Tailscale



**Quản lý mạng:** Bảng điều khiển quản trị (login.tailscale.com) cho phép bạn quản lý thiết bị, xem kết nối và cấu hình quy tắc truy cập.



**MagicDNS:** Tự động phân giải tên thiết bị (ví dụ: `raspberrypi.tailnet.ts.net`) để tránh ghi nhớ địa chỉ IP.



**ACL và kiểm soát truy cập:** Xác định chính xác ai có thể truy cập vào nội dung nào trong mạng của bạn thông qua các quy tắc JSON, lý tưởng để cô lập một số thiết bị nhất định hoặc hạn chế quyền truy cập vào các dịch vụ cụ thể.



**Chia sẻ thiết bị cho phép bạn mời ai đó truy cập vào một máy cụ thể mà không cần cấp cho họ quyền truy cập vào toàn bộ mạng của bạn.



**Bộ định tuyến mạng con:** Máy Tailscale có thể hoạt động như một cổng cho toàn bộ mạng con, cho phép truy cập vào các thiết bị không phải Tailscale (IoT, máy in, v.v.) thông qua một máy được cấu hình duy nhất.



**Nút thoát:** Sử dụng máy như một cổng Internet để thoát bằng IP của nó. Hữu ích cho Wi-Fi công cộng hoặc để bỏ qua các hạn chế về mặt địa lý.



**Taildrop:** Một giải pháp thay thế an toàn cho AirDrop, cho phép bạn chuyển tệp giữa các thiết bị Tailscale của mình, bất kể nền tảng hoặc vị trí của chúng. Không giống như AirDrop, chỉ giới hạn trong hệ sinh thái Apple và khoảng cách vật lý, Taildrop hoạt động giữa tất cả các thiết bị của bạn (Windows, Mac, Linux, Android, iOS), ngay cả khi chúng ở các quốc gia khác nhau. Tệp được chuyển trực tiếp giữa các thiết bị với mã hóa đầu cuối, mà không cần thông qua máy chủ trung tâm. Sử dụng dòng lệnh `tailscale file cp` hoặc ứng dụng đồ họa Interface tùy thuộc vào hệ thống của bạn.



### 5.2 So sánh với các giải pháp khác



**Vs OpenVPN:** Tailscale dễ cấu hình hơn nhiều (không cần mở cổng, không cần quản lý chứng chỉ) nhưng lại phụ thuộc vào dịch vụ của bên thứ ba. OpenVPN có thể kiểm soát hoàn toàn nhưng đòi hỏi nhiều chuyên môn hơn.



**Là đối thủ cạnh tranh trực tiếp, ZeroTier hoạt động ở Layer 2 (Ethernet), cho phép phát sóng/phát đa hướng, trong khi Tailscale hoạt động ở Layer 3 (IP). ZeroTier cung cấp tính linh hoạt mạng lớn hơn, trong khi Tailscale ưu tiên tính đơn giản khi sử dụng.



**Vs Tor:** Tor cung cấp tính ẩn danh mà Tailscale không có, nhưng chậm hơn nhiều. Tor phi tập trung và không yêu cầu tài khoản, trong khi Tailscale nhanh hơn và cung cấp trải nghiệm giống như LAN.



**So với hướng dẫn sử dụng WireGuard:** Tailscale tự động hóa mọi quản lý khóa và kết nối mà WireGuard raw yêu cầu bạn xử lý thủ công. Về cơ bản, nó là WireGuard + một Layer quản lý được đơn giản hóa.



Tóm lại, Tailscale tự định vị mình là một giải pháp hiện đại, hướng đến sự đơn giản, lý tưởng cho mục đích sử dụng cá nhân và nhóm nhỏ. Đối với những người theo chủ nghĩa thuần túy muốn kiểm soát hoàn toàn, Headscale cung cấp giải pháp thay thế tự lưu trữ.



## 6. Kết luận



**Lợi ích của Tailscale:** Tailscale cung cấp một số lợi ích khi tự lưu trữ:





- Đơn giản và hiệu suất** - Cài đặt nhanh trên mọi nền tảng mà không cần cấu hình mạng phức tạp. Lưu lượng đi theo đường dẫn trực tiếp nhất giữa các máy của bạn (P2P mesh), với hiệu suất của giao thức WireGuard và không có máy chủ trung tâm nào giới hạn thông lượng.
- Bảo mật và tính linh hoạt** - Mã hóa đầu cuối, giảm bề mặt tấn công và các tính năng nâng cao (ACL, xác thực SSO/MFA). Hoạt động ngay cả sau NAT hoặc khi di chuyển, với bộ định tuyến mạng con và nút thoát để điều chỉnh mạng theo nhu cầu của bạn.



**Giới hạn:** Ngoài ra, hãy lưu ý:





- Phụ thuộc bên ngoài** - Trong phiên bản chuẩn, dịch vụ này dựa trên cơ sở hạ tầng Tailscale Inc. Sự phụ thuộc này có thể được bỏ qua thông qua Headscale (giải pháp thay thế tự lưu trữ).
- Các hạn chế khác** - Mã nguồn đóng một phần, giới hạn của phiên bản miễn phí đối với một số mục đích sử dụng nâng cao, không hỗ trợ Layer 2 (phát/phát đa hướng) và cần có quyền truy cập Internet để thiết lập kết nối.



**Tailscale lý tưởng cho các máy chủ cá nhân và nhóm nhỏ, các nhà phát triển cần truy cập vào các tài nguyên phân tán, người mới bắt đầu sử dụng VPN và người dùng di động. Đối với các công ty yêu cầu kiểm soát hoàn toàn, các giải pháp khác như Headscale hoặc WireGuard trực tiếp có thể được ưu tiên.



**Khám phá Headscale để có khả năng tự lưu trữ hoàn toàn, tích hợp API và DevOps (Terraform) hoặc các giải pháp thay thế như Innernet (tương tự nhưng tự lưu trữ hoàn toàn) và Netmaker.



Tailscale là một công cụ thiết yếu để tự lưu trữ, nhờ tính đơn giản và hiệu quả, giúp cơ sở hạ tầng riêng tư của bạn dễ truy cập như thể đang ở trên đám mây, đồng thời vẫn có thể kiểm soát tại nhà.



## 7. Tài nguyên hữu ích



### Tài liệu chính thức





- Trung tâm tài liệu Tailscale**: [docs.tailscale.com](https://docs.tailscale.com) - Tài liệu đầy đủ bằng tiếng Anh, hướng dẫn cài đặt, hướng dẫn sử dụng và tài liệu tham khảo kỹ thuật.
- Tailscale hoạt động như thế nào**: [Tailscale hoạt động như thế nào](https://tailscale.com/blog/how-tailscale-works) - Bài viết chi tiết giải thích cách thức hoạt động bên trong của Tailscale.
- Nhật ký thay đổi**: [tailscale.com/changelog](https://tailscale.com/changelog) - Theo dõi các bản cập nhật và tính năng mới.



### Hướng dẫn thực tế





- Hướng dẫn về Homelab**: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Hướng dẫn cụ thể về việc tự lưu trữ.
- Cấu hình Nút thoát**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Hướng dẫn chi tiết về cách cấu hình Nút thoát.
- Sử dụng Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Chuyển tệp giữa các thiết bị Tailscale.



### So sánh





- Tailscale so với các giải pháp khác**: [tailscale.com/compare](https://tailscale.com/compare) - So sánh chi tiết với các giải pháp mạng và VPN khác (ZeroTier, OpenVPN, v.v.).



### Cộng đồng





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Thảo luận, câu hỏi và phản hồi.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Mã nguồn của khách hàng, nơi theo dõi quá trình phát triển và báo cáo sự cố.
- Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Cộng đồng người dùng và nhà phát triển.



Tailscale thường xuyên cung cấp nội dung và tính năng mới. Hãy xem [blog chính thức](https://tailscale.com/blog/) của họ để biết tin tức và nghiên cứu tình huống mới nhất.