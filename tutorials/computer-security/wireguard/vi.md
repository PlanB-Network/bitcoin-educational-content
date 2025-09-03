---
name: WireGuard
description: Thiết lập WireGuard VPN trên Debian và Windows
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Florian BURNEL được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã được chỉnh sửa.*



___



## I. Trình bày



Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách cấu hình VPN dựa trên WireGuard, một giải pháp VPN mã nguồn mở miễn phí giúp tăng cường hiệu suất mà không bỏ qua tính bảo mật.



WireGuard là một giải pháp tương đối mới, đã có sẵn dưới dạng bản phát hành ổn định từ tháng 3 năm 2020 và đã vinh dự được tích hợp trực tiếp vào **nhân Linux kể từ phiên bản 5.6**. Điều này không ngăn cản việc nó có thể được truy cập từ các bản phân phối Linux cũ hơn sử dụng một phiên bản nhân khác. So với các giải pháp như OpenVPN và IPSec, WireGuard dễ sử dụng hơn và nhanh hơn nhiều, như chúng ta sẽ thấy ở cuối bài viết này.



Một số điểm chính về WireGuard:





- Đơn giản, nhẹ và cực kỳ hiệu quả!
- Hoạt động chỉ sử dụng UDP (có thể là một bất lợi khi vượt qua một số tường lửa)
- Hoạt động theo mô hình ngang hàng thay vì mô hình máy khách-máy chủ
- Xác thực bằng khóa Exchange, theo nguyên tắc tương tự như SSH với khóa riêng tư/công khai
- Sử dụng một số thuật toán: mã hóa đối xứng với ChaCha20, xác thực tin nhắn với Poly1305, cũng như các thuật toán khác như Curve25519, BLAKE2 và SipHash24
- Hỗ trợ cả IPv4 và IPv6
- Đa nền tảng: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (và được triển khai trong ProtonVPN)
- Chỉ có 4.000 dòng mã, so với hàng trăm nghìn dòng mã của các giải pháp khác



Về phần mật mã, các thuật toán khác nhau được sử dụng đều được lựa chọn kỹ lưỡng, kiểm tra theo nhiều cách và được các nhà nghiên cứu bảo mật chuyên ngành kiểm tra.



Trang web chính thức của dự án: [wireguard.com](https://www.wireguard.com/)



Bạn có bị thuyết phục bởi giải pháp này sau khi đọc phần giới thiệu không? Việc còn lại là đọc tiếp thôi!



## II. Sơ đồ Lab WireGuard



Trước khi tôi trình bày bài thực hành thiết lập WireGuard, bạn nên biết rằng bạn có thể hình dung **sử dụng WireGuard để kết nối hai cơ sở hạ tầng từ xa**, cũng như **kết nối một máy khách từ xa với một cơ sở hạ tầng như mạng công ty hoặc mạng gia đình**. Điều này cũng tương tự như với OpenVPN, như chúng ta đã thấy gần đây trong hướng dẫn "[OpenVPN trên Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Nếu WireGuard không được thiết lập trực tiếp trên bộ định tuyến hoặc tường lửa, như có thể thực hiện với OpenWRT, bạn sẽ cần thiết lập chuyển tiếp cổng để luồng dữ liệu đến được cặp WireGuard.



![Image](assets/fr/034.webp)



Bây giờ tôi sẽ kể cho bạn nghe về phòng thí nghiệm của tôi và những gì chúng ta sẽ thiết lập ngày hôm nay.



Tôi sẽ sử dụng máy Debian 11 làm máy chủ WireGuard và máy khách Windows làm máy khách WireGuard VPN. Mặc dù việc nói về mối quan hệ máy khách-máy chủ hơi gây hiểu lầm, vì **WireGuard hoạt động theo mô hình "ngang hàng"**. Cách gọi này hơi sai khi bạn đang cố gắng thiết lập kết nối "máy khách-trang web". Thay vào đó, giả sử tôi sẽ có hai cặp hoặc **hai điểm kết nối WireGuard** nếu bạn muốn: một trên Debian 11 và một trên Windows.



Hai cặp này có thể giao tiếp với nhau theo cả hai hướng, nghĩa là từ máy Windows của tôi, tôi có thể truy cập mạng LAN từ xa của máy Debian 11 và ngược lại: tất cả phụ thuộc vào cấu hình của đường hầm và tường lửa của đối tác WireGuard.



Trong ví dụ này, tôi sẽ tập trung vào trường hợp sau: **từ Windows Peer 1 được kết nối với mạng gia đình, tôi muốn truy cập vào mạng công ty để truy cập máy chủ của công ty thông qua đường hầm WireGuard VPN**. Sơ đồ sau được thể hiện như sau:



![Image](assets/fr/035.webp)



Về mặt địa chỉ IP, điều này đưa ra:





- Mạng gia đình**: 192.168.1.0/24
- Mạng công ty**: 192.168.100.0/24
- Mạng đường hầm WireGuard**: 192.168.110.0/24


+ IP Address của Peer 1 (Windows) trong đường hầm: 192.168.110.2/24


+ IP Address của Peer 2 (Debian) trong đường hầm: 192.168.110.121/24



Vậy là xong! Cùng bắt tay vào cấu hình thôi!



**Lưu ý: theo mặc định, WireGuard hoạt động ở chế độ UDP trên **cổng 51820**.



## III Cài đặt và cấu hình máy chủ WireGuard



Tôi sẽ sử dụng thuật ngữ "máy khách" cho máy Windows và "máy chủ" cho máy Debian trong hướng dẫn này, vì mặc dù là ngang hàng nhưng nó có vẻ có ý nghĩa hơn.



### A. Cài đặt WireGuard trên Debian 11



Gói cài đặt WireGuard có sẵn trong kho lưu trữ chính thức của Debian 11, vì vậy tất cả những gì chúng ta phải làm là cập nhật bộ đệm gói và cài đặt nó:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Phần máy chủ WireGuard sẽ được cài đặt cùng với nhiều công cụ khác nhau cung cấp quyền truy cập vào các lệnh hữu ích để quản lý cấu hình.



### B. Lắp đặt Interface WireGuard



Khi sử dụng **lệnh "wg "**, chúng ta cần generate một khóa riêng tư và một khóa công khai: điều cần thiết để xác thực giữa hai cặp, tức là máy chủ và máy khách (cũng sẽ cần một cặp khóa).



Chúng ta sẽ tạo khóa riêng "**/etc/wireguard/wg-private.key**" và khóa công khai "**/etc/wireguard/wg-public.key**" bằng chuỗi lệnh này:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Giá trị của khóa công khai sẽ được trả về trong bảng điều khiển. Trong tệp cấu hình WireGuard, chúng ta cần **thêm giá trị của khóa riêng tư**. Để lấy giá trị này, hãy nhập lệnh bên dưới và sao chép giá trị:



```
sudo cat /etc/wireguard/wg-private.key
```



Đã đến lúc tạo tệp cấu hình trong "**/etc/wireguard/**". Ví dụ: chúng ta có thể đặt tên tệp này là "**wg0.conf**", nếu chúng ta nghĩ rằng mạng Interface được liên kết với WireGuard sẽ là "wg0", theo cùng nguyên tắc với "eth0" chẳng hạn.



```
sudo nano /etc/wireguard/wg0.conf
```



Trong tệp này, trước tiên chúng ta phải thêm nội dung sau (chúng ta sẽ quay lại để hoàn thiện sau):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Phần `[Interface]` được sử dụng để khai báo phần máy chủ. Dưới đây là một số thông tin:





- Address**: IP Address của Interface WireGuard trong đường hầm VPN (mạng con khác với mạng LAN từ xa)
- SaveConfig**: cấu hình được lưu trữ (và bảo vệ) miễn là Interface còn hoạt động
- ListenPort**: Cổng lắng nghe của WireGuard. Trong trường hợp này, 51820 là cổng mặc định, nhưng bạn có thể tùy chỉnh nó.
- PrivateKey**: giá trị khóa riêng của máy chủ của chúng tôi (*wg-private.key*)



Lưu tệp và đóng lại. Với lệnh "**wg-quick**", chúng ta có thể khởi động Interface này bằng cách chỉ định tên của nó (wg0, vì tệp có tên là wg0.conf):



```
sudo wg-quick up wg0
```



Nếu bạn liệt kê các địa chỉ IP của máy chủ Debian 11, bạn sẽ thấy một Interface mới có tên "wg0" với IP Address được xác định trong tệp cấu hình:



```
ip a
```



![Image](assets/fr/027.webp)



Theo tinh thần tương tự, chúng ta có thể hiển thị cấu hình "wg0" của Interface thông qua lệnh "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Cuối cùng, chúng ta cần kích hoạt tính năng khởi động tự động của WireGuard Interface wg0:



```
sudo systemctl enable wg-quick@wg0.service
```



Hiện tại, chúng ta sẽ bỏ qua phần cấu hình phía máy chủ của WireGuard.



### C. Bật Chuyển tiếp IP



Để máy Debian 11 của chúng tôi có thể **định tuyến các gói tin giữa các mạng khác nhau (như bộ định tuyến)**, tức là giữa mạng VPN và mạng cục bộ, chúng tôi cần bật [Chuyển tiếp IP](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Theo mặc định, tính năng này bị tắt.



Sửa đổi tệp cấu hình này:



```
sudo nano /etc/sysctl.conf
```



Thêm chỉ thị sau vào cuối tệp và lưu:



```
net.ipv4.ip_forward = 1
```



Chỉ có vậy thôi.



### D. Bật IP Masquerade



Để máy chủ của chúng tôi định tuyến các gói tin chính xác và để mạng LAN từ xa có thể truy cập được vào máy Windows, chúng tôi cần kích hoạt IP Masquerade trên máy chủ Debian. Đây là một dạng kích hoạt NAT. Tôi sẽ thực hiện cấu hình này trên tường lửa Linux thông qua UFW, mà tôi đã quen sử dụng ([hướng dẫn ufw trên Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Nếu bạn chưa có UFW và muốn thiết lập nó (bạn cũng có thể sử dụng Nftables), hãy bắt đầu bằng cách cài đặt:



```
sudo apt install ufw
```



Trước hết, bạn cần bật SSH để không mất quyền kiểm soát máy chủ từ xa (điều chỉnh số cổng):



```
sudo ufw allow 22/tcp
```



Cổng 51820 trong UDP cũng phải được cấp phép vì chúng tôi sử dụng cổng này cho WireGuard (một lần nữa, hãy điều chỉnh số cổng):



```
sudo ufw allow 51820/udp
```



Tiếp theo, chúng ta sẽ tiếp tục cấu hình để bật tính năng giả mạo IP. Để thực hiện việc này, chúng ta cần lấy tên của Interface đang được kết nối với mạng cục bộ. Nếu bạn không biết tên, hãy chạy lệnh "ip a" để xem tên của card. Trong trường hợp của tôi, đó là card "**ens192**".



![Image](assets/fr/036.webp)



Chúng ta sẽ sử dụng thông tin này. Chỉnh sửa tệp sau:



```
sudo nano /etc/ufw/before.rules
```



Thêm các dòng này vào cuối tệp để **bật tính năng ngụy trang IP trên Interface ens192** (điều chỉnh tên Interface) trong chuỗi POSTROUTING của bảng NAT trên tường lửa cục bộ của chúng tôi:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Hình ảnh cho thấy:



![Image](assets/fr/037.webp)



Giữ nguyên tệp cấu hình này và tiến hành bước tiếp theo. 😉



### E. Cấu hình tường lửa Linux cho WireGuard



Vẫn trong cùng tệp cấu hình, chúng ta sẽ khai báo mạng công ty "192.168.100.0/24" để có thể liên hệ. Dưới đây là hai quy tắc cần thêm (tốt nhất là sau phần "*# ok icmp code for FORWARD*" để nhóm các quy tắc lại với nhau):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Nếu bạn chỉ muốn cấp quyền cho một máy chủ, ví dụ "192.168.100.11", thì rất dễ:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Bây giờ bạn có thể lưu và đóng tệp. Việc còn lại là kích hoạt UFW và khởi động lại dịch vụ để áp dụng các thay đổi của chúng tôi:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Phần đầu tiên của quá trình cấu hình máy chủ Debian hiện đã hoàn tất.



## IV. Máy khách WireGuard dành cho Windows



Ứng dụng khách WireGuard có sẵn cho Windows, macOS, Android, v.v... Đây là một tin tuyệt vời. Tất cả các bản tải xuống đều có sẵn trên trang này: [Ứng dụng khách WireGuard](https://www.wireguard.com/install/). Trong ví dụ này, tôi sẽ thiết lập ứng dụng khách trên Windows. Để thiết lập ứng dụng khách WireGuard trên Linux, hãy làm theo nguyên tắc tương tự như khi tạo tệp wg0.conf trên máy Debian (không bao gồm tất cả các thông số NAT, v.v.).



### A. Cài đặt máy khách WireGuard Windows



Sau khi tải xuống tệp thực thi hoặc gói MSI, việc cài đặt rất đơn giản: chỉ cần khởi chạy trình cài đặt và... thế là xong! 🙂



![Image](assets/fr/038.webp)



### B. Tạo hồ sơ WireGuard



Bắt đầu bằng cách mở phần mềm để tạo một đường hầm mới. Để thực hiện việc này, hãy nhấp vào mũi tên bên phải nút "**Thêm đường hầm**" và nhấp vào nút "**Thêm đường hầm trống**".



![Image](assets/fr/028.webp)



Một cửa sổ cấu hình sẽ mở ra. Mỗi khi một cấu hình đường hầm mới được tạo, WireGuard sẽ tạo một cặp khóa riêng/công khai dành riêng cho cấu hình này. **Trong cấu hình này, chúng ta cần khai báo "peer", tức là máy chủ từ xa:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Chúng ta cần hoàn tất cấu hình này, cụ thể là khai báo IP Address trên Interface này (*Address*), đồng thời khai báo máy chủ WireGuard từ xa thông qua khối [Peer]. Hình ảnh bên dưới sẽ giúp bạn nhớ lại tệp cấu hình chúng ta đã tạo trên máy chủ Linux.



Hãy bắt đầu với khối `[Interface]`, thêm IP Address "**192.168.110.2**"; hãy nhớ rằng máy chủ có IP Address "**192.168.110.121**" trên phân đoạn mạng này. Điều này sẽ cho kết quả:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Tiếp theo, chúng ta cần khai báo khối "Peer" với ba thuộc tính, tạo ra cấu hình này:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Trong hình ảnh:



![Image](assets/fr/029.webp)



**Một vài giải thích về khối [Peer]:





- PublicKey**: đây là khóa công khai của máy chủ WireGuard Debian 11 (bạn có thể lấy giá trị của khóa này bằng lệnh "*sudo wg*")
- AllowedIPs**: đây là các địa chỉ IP/mạng con có thể truy cập thông qua mạng WireGuard VPN này, trong trường hợp này là mạng con dành riêng cho WireGuard VPN của tôi (*192.168.110.0/24*) và mạng LAN từ xa của tôi (*192.168.100.0/24*)
- Điểm cuối**: đây là IP Address của máy chủ Debian 11, vì đây là điểm kết nối WireGuard của chúng tôi (bạn sẽ cần chỉ định IP công khai Address)



Cuối cùng, nhập tên vào trường "**Tên**" (không có khoảng trắng) và sao chép và dán khóa công khai của máy khách, vì chúng ta sẽ cần khai báo khóa này trên máy chủ. Nhấp vào "**Đăng ký**".



### C. Khai báo máy khách trên máy chủ WireGuard



Đã đến lúc quay lại máy chủ Debian để khai báo "**Peer**", tức là máy tính Windows của chúng ta, trong cấu hình WireGuard. Trước hết, chúng ta cần **dừng Interface "wg0"** để sửa đổi cấu hình của nó:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Tiếp theo, sửa đổi tệp cấu hình đã tạo trước đó:



```
sudo nano /etc/wireguard/wg0.conf
```



Trong tệp này, sau khối `[Interface]`, chúng ta cần khai báo khối `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Khối [Peer] này chứa khóa công khai của PC chạy Windows 10 (**PublicKey**) và IP Address của Interface của PC (**AllowedIPs**): máy chủ sẽ giao tiếp trong đường hầm WireGuard này chỉ để liên hệ với máy khách Windows, do đó có giá trị "**192.168.110.2/32**".



Việc còn lại là lưu tệp (*CTRL+O rồi Enter rồi CTRL+X qua Nano*). Khởi chạy lại Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Để kiểm tra xem khai báo ngang hàng có hoạt động không, bạn có thể sử dụng lệnh này:



```
sudo wg show
```



Sau khi máy chủ từ xa thiết lập kết nối WireGuard, IP Address của máy chủ đó sẽ được chuyển lên giá trị "điểm cuối".



![Image](assets/fr/033.webp)



Cuối cùng, chúng ta sẽ bảo mật các tệp cấu hình để hạn chế quyền truy cập root:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Kết nối WireGuard đầu tiên



Bây giờ cấu hình đã sẵn sàng, chúng ta có thể bắt đầu từ máy tính Windows. Để thực hiện việc này, trong ứng dụng khách "**WireGuard**", hãy nhấp vào nút "**Kích hoạt**": kết nối sẽ **chuyển từ "Tắt" sang "Bật"**, nhưng điều đó không có nghĩa là nó sẽ hoạt động. Tất cả phụ thuộc vào việc cấu hình của bạn có chính xác hay không. **Khi kết nối được thiết lập, hai máy của chúng ta sẽ giao tiếp với nhau thông qua WireGuard Interface được cấu hình ở mỗi bên!



![Image](assets/fr/030.webp)



Trong trường hợp có sự cố, thông tin này sẽ hiển thị trong tab "**Nhật ký**". Hai máy chủ sẽ gửi gói tin Exchange thường xuyên để kiểm tra trạng thái kết nối, do đó sẽ xuất hiện thông báo "*Nhận gói tin duy trì kết nối từ máy ngang hàng 1*".



![Image](assets/fr/031.webp)



Nếu tab "**Nhật ký**" của WireGuard hiển thị thông báo như bên dưới, bạn cần kiểm tra xem khóa công khai được khai báo ở cả hai bên có chính xác không.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Từ máy tính từ xa, tôi có thể ping địa chỉ IP Address của Interface WireGuard ở phía máy chủ cũng như máy chủ lưu trữ trên mạng LAN từ xa của tôi.



![Image](assets/fr/032.webp)



### E. Hiệu suất: OpenVPN so với WireGuard



Từ máy tính từ xa được kết nối với VPN WireGuard, tôi có thể truy cập máy chủ tệp và truyền tệp qua [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), để xem tốc độ truyền. **Với WireGuard, tôi đạt tốc độ tối đa khoảng 45 Mb/giây, rất tuyệt vời vì tôi dùng WiFi.



![Image](assets/fr/025.webp)



Trong cùng điều kiện, nhưng lần này thông qua kết nối OpenVPN (UDP), với cùng thao tác, thông lượng lại hoàn toàn khác biệt: khoảng 3 MB/giây. Sự khác biệt là rõ ràng!



![Image](assets/fr/026.webp)



Điều này thật thú vị, vì nếu chẳng hạn, bạn chuyển từ kết nối WiFi sang kết nối 4G/5G, việc kết nối lại sẽ diễn ra nhanh đến mức sự gián đoạn sẽ không thể nhận thấy.



### F. Phần thưởng: đường hầm đầy đủ WireGuard



Với cấu hình hiện tại, một phần lưu lượng sẽ chạy qua VPN, phần còn lại chạy qua kết nối Internet của khách hàng, bao gồm cả việc duyệt web. Nếu chúng ta muốn chuyển sang chế độ đường hầm đầy đủ của WireGuard, để mọi thứ đều đi qua đường hầm VPN, chúng ta cần thực hiện một vài thay đổi trong cấu hình....



Đầu tiên, bạn cần cài đặt gói "resolvconf" trên:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Sau khi thực hiện xong, bạn cần sửa đổi cấu hình "wg0.conf" trên máy Debian: dừng Interface, sửa đổi và khởi động lại.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Tiếp theo, **trong khối `[Interface]`, chúng ta thêm máy chủ DNS sẽ sử dụng**. Trong trường hợp của tôi, đó là bộ điều khiển miền của phòng thí nghiệm, nhưng chúng ta cũng có thể cài đặt Bind9 trên máy Debian để có trình phân giải cục bộ.



```
DNS = 192.168.100.11
```



Lưu tệp, sau đó khởi động lại Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Cuối cùng, trong cấu hình đường hầm trên máy trạm Windows 10, bạn cần sửa đổi phần "AllowedIPs" để chỉ ra rằng mọi thứ phải đi qua đường hầm. Thay thế:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Qua:



```
AllowedIPs = 0.0.0.0/0
```



Bạn có thể thấy rằng thao tác này cũng kích hoạt tùy chọn "**Kill switch*".



![Image](assets/fr/040.webp)



Cuối cùng, tôi đã tận dụng đường hầm đầy đủ này để thực hiện một thử nghiệm lưu lượng nhỏ, kết quả được hiển thị bên dưới:



![Image](assets/fr/039.webp)



Cấu hình của WireGuard khá đơn giản và dễ hiểu, và trên hết là dễ bảo trì. **WireGuard được coi là tương lai của VPN**, vì vậy chúng ta nên theo dõi sát sao! Chúng ta cũng có thể thấy lợi ích đáng kể về mặt hiệu suất, một lợi thế rất lớn của WireGuard so với OpenVPN.



Tài liệu bổ sung:





- [Man - Lệnh wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Lệnh wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**WireGuard VPN của bạn đã hoạt động! Xin chúc mừng!