---
name: OPNsense
description: Làm thế nào để cài đặt và cấu hình tường lửa OPNsense?
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Florian BURNEL được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã được chỉnh sửa.*



___



## I. Trình bày



Trong hướng dẫn này, chúng ta sẽ tìm hiểu về tường lửa mã nguồn mở OPNsense. Chúng ta sẽ xem xét các tính năng chính, điều kiện tiên quyết và cách cài đặt giải pháp dựa trên FreeBSD này.



Trước khi bắt đầu, bạn nên biết rằng **OPNsense và pfSense đều là tường lửa mã nguồn mở** dựa trên FreeBSD. Có thể nói pfSense gần như là anh cả của OPNsense, vì OPNsense là Fork được tạo ra vào năm 2015. Cuối cùng, điều quan trọng cần lưu ý là kể từ năm 2017, **OPNsense đã chuyển sang HardenedBSD thay vì FreeBSD**. HardenedBSD là phiên bản nâng cao của FreeBSD, với các tính năng bảo mật tiên tiến.



OPNsense nổi bật với giao diện người dùng Interface hiện đại hơn và **tần suất cập nhật thường xuyên hơn**. Thực tế, lịch trình cập nhật của OPNsense bao gồm hai bản phát hành chính mỗi năm, được cập nhật khoảng hai tuần một lần (dẫn đến các bản phát hành phụ). Việc theo dõi này rất thú vị khi so sánh với pfSense, nếu chúng ta xem xét các phiên bản cộng đồng của các giải pháp này.



![Image](assets/fr/050.webp)



## II. Các tính năng của OPNsense



OPNsense là hệ điều hành được thiết kế để hoạt động như tường lửa và bộ định tuyến, mặc dù có nhiều tính năng và có thể mở rộng bằng cách cài đặt các gói bổ sung. Phù hợp cho mục đích sử dụng sản xuất, OPNsense chủ yếu được sử dụng cho bảo mật mạng và quản lý luồng.



### A. Các tính năng chính



Sau đây là một số tính năng chính của OPNsense:





- Tường lửa và NAT**: OPNsense cung cấp chức năng tường lửa trạng thái nâng cao với tính năng lọc trạng thái cũng như khả năng chuyển đổi Address (NAT) mạng.





- DNS/DHCP**: OPNsense có thể được cấu hình để quản lý các dịch vụ DNS và DHCP trên mạng. Nó có thể hoạt động như một máy chủ DHCP, nhưng cũng có thể được sử dụng như một bộ phân giải DNS cho các máy trong mạng cục bộ. Dnsmasq cũng được tích hợp theo mặc định.





- VPN**: OPNsense hỗ trợ một số giao thức VPN, bao gồm IPsec, OpenVPN và WireGuard, cho phép kết nối an toàn để truy cập từ xa vào các máy trạm di động hoặc kết nối trang web.





- Proxy web**: OPNsense bao gồm một proxy web để kiểm soát và lọc truy cập Internet. Nó cũng có thể được sử dụng để lọc nội dung và quản lý truy cập mạng.





- Quản lý băng thông (QoS)**: OPNsense cung cấp các tính năng quản lý Chất lượng dịch vụ (QoS) để ưu tiên lưu lượng mạng và quản lý băng thông mạng tốt hơn.





- Cổng thông tin cố định**: tính năng này cho phép bạn quản lý quyền truy cập của người dùng vào mạng thông qua trang xác thực (cơ sở cục bộ, chứng từ, v.v.). Đây là tính năng thường được triển khai cho mạng Wi-Fi công cộng.





- IDS/IPS**: OPNsense tích hợp Suricata để cung cấp chức năng phát hiện và ngăn chặn xâm nhập (IDS/IPS) nhằm bảo vệ mạng khỏi các cuộc tấn công.





- Tính khả dụng cao (CARP)**: OPNsense hỗ trợ CARP (*Giao thức dự phòng Address chung*) để có tính khả dụng cao giữa nhiều tường lửa OPNsense, đảm bảo dịch vụ vẫn hoạt động ngay cả khi phần cứng bị lỗi.





- Báo cáo và Giám sát**: OPNsense cung cấp các công cụ báo cáo và giám sát theo thời gian thực để theo dõi hiệu suất mạng (với NetFlow) và phát hiện các sự cố tiềm ẩn, nhờ vào việc tạo nhật ký. Nhật ký này bao gồm cả đồ họa. Công cụ Monit được tích hợp vào OPNsense và cho phép giám sát tường lửa.



### B. Các gói bổ sung



Đây chỉ là tổng quan về các tính năng được cung cấp bởi OPNsense. Ngoài ra, **danh mục gói** có thể truy cập từ OPNsense Interface cho phép bạn **làm phong phú thêm tường lửa với các chức năng bổ sung**. Các chức năng này bao gồm máy khách ACME, tác nhân Wazuh, dịch vụ NTP Chrony và Caddy làm proxy ngược.



![Image](assets/fr/051.webp)



## III. Điều kiện tiên quyết của OPNsense



Trước hết, bạn cần quyết định nơi bạn sẽ cài đặt OPNsense. Có một số giải pháp khả thi, bao gồm cài đặt trên:





- Một chương trình quản lý siêu máy ảo như Hyper-V, Proxmox, VMware ESXi, v.v.
- Một máy tính như một hệ thống *trần trụi*. Đây có thể là một máy tính mini hoạt động như một tường lửa.



Bạn cũng có thể mua **thiết bị gắn trên giá OPNsense** thông qua cửa hàng trực tuyến của chúng tôi.



Bạn cần lưu ý đến các tài nguyên phần cứng cần thiết để chạy OPNsense. Thông tin này được trình bày chi tiết trên [trang tài liệu này](https://docs.opnsense.org/manual/hardware.html).



**Tài nguyên tối thiểu và khuyến nghị cho sản xuất:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Cuối cùng, **yêu cầu tài nguyên của bạn phụ thuộc chủ yếu vào số lượng kết nối cần quản lý**, và do đó phụ thuộc vào **yêu cầu băng thông** của bạn. Ngoài ra, bạn cần **lưu ý các dịch vụ sẽ được kích hoạt và sử dụng** (proxy, phát hiện xâm nhập, v.v...) vì chúng có thể ngốn nhiều CPU và/hoặc RAM.



Bạn cũng sẽ cần ảnh ISO cài đặt OPNsense, có thể tải xuống từ [trang web chính thức](https://opnsense.org/download/). Để cài đặt trên máy ảo (VM), hãy chọn "**dvd**" làm loại ảnh để lấy ảnh ISO (và làm bất cứ điều gì bạn muốn với nó...). Để cài đặt thông qua khóa USB có thể khởi động, hãy chọn tùy chọn "**vga**" để lấy tệp "**.img**".



![Image](assets/fr/048.webp)



Bạn cũng sẽ cần một máy tính để quản lý và thử nghiệm OPNsense.



## IV. Cấu hình mục tiêu



Mục tiêu của chúng tôi là





- Tạo một mạng ảo nội bộ (192.168.10.0/24 - LAN)**, có thể truy cập Internet thông qua tường lửa OPNsense. Đối với mục đích sử dụng sản xuất, đây có thể là mạng cục bộ, cáp và/hoặc Wi-Fi của bạn.
- Kích hoạt và cấu hình NAT** để các máy ảo trong mạng ảo nội bộ có thể truy cập Internet
- Kích hoạt và cấu hình máy chủ DHCP trên OPNsense** để phân phối cấu hình IP cho các máy trong tương lai được kết nối với mạng ảo nội bộ
- Cấu hình tường lửa** để chỉ cho phép luồng dữ liệu LAN tới WAN đi qua HTTP (80) và HTTPS (443).
- Cấu hình tường lửa** để cho phép mạng LAN ảo sử dụng OPNsense làm trình phân giải DNS (53).



Nếu bạn đang sử dụng nền tảng Hyper-V, bạn sẽ thấy thông tin sau:



![Image](assets/fr/033.webp)



## V. Cài đặt tường lửa OPNsense



### A. Chuẩn bị ổ USB có thể khởi động



Bước đầu tiên là chuẩn bị phương tiện cài đặt: **USB có thể khởi động với OPNsense**. Tất nhiên, điều này là tùy chọn nếu bạn đang làm việc trong môi trường ảo, nhưng trong mọi trường hợp, bạn cần tải xuống ảnh ISO cài đặt OPNsense.



Sau khi tải xuống, bạn sẽ nhận được **một tệp lưu trữ chứa hình ảnh ở định dạng ".img". Bạn có thể **tạo ổ USB khởi động** bằng nhiều ứng dụng khác nhau, bao gồm **balenaEtcher**: cực kỳ dễ sử dụng. Hơn nữa, ứng dụng sẽ nhận dạng hình ảnh trong tệp lưu trữ, vì vậy bạn không cần phải giải nén trước.





- [Tải xuống balenaEtcher](https://etcher.balena.io/)



Sau khi cài đặt ứng dụng, hãy chọn hình ảnh, ổ USB của bạn rồi nhấp vào "Flash! Đợi một lát.



![Image](assets/fr/049.webp)



Bây giờ bạn đã sẵn sàng để cài đặt.



### B. Cài đặt hệ thống OPNsense



Khởi động máy chủ lưu trữ OPNsense. Bạn sẽ thấy trang chào mừng tương tự như bên dưới. Trong vài giây, màn hình hiển thị sẽ hiển thị trong cửa sổ. Hãy để quá trình diễn ra tự động...



![Image](assets/fr/019.webp)



Hình ảnh OPNsense được tải lên máy để có thể truy cập hệ thống ở chế độ "**trực tiếp**", tức là được lưu trữ tạm thời trong bộ nhớ.



![Image](assets/fr/025.webp)



Sau đó, bạn sẽ đến Interface tương tự như bên dưới. Đăng nhập bằng tên đăng nhập "**installer**" và mật khẩu "**opnsense**". Xin lưu ý rằng bàn phím hiện tại là **QWERTY**. Lúc này, chúng ta sẽ **bắt đầu quá trình cài đặt OPNsense**.



![Image](assets/fr/026.webp)



Một trình hướng dẫn mới sẽ xuất hiện trên màn hình. Bước đầu tiên là chọn bố cục bàn phím tương ứng với cấu hình của bạn. Đối với bàn phím AZERTY, hãy chọn tùy chọn "**Tiếng Pháp (phím nhấn)**" từ danh sách, sau đó nhấp đúp**.



![Image](assets/fr/027.webp)



Bước thứ hai là chọn tác vụ cần thực hiện. Ở đây, chúng ta sẽ thực hiện cài đặt bằng **hệ thống tệp ZFS**. Hãy chọn dòng "**Cài đặt (ZFS)**" và xác nhận bằng **Enter**.



![Image](assets/fr/028.webp)



Ở bước thứ ba, hãy chọn "**stripe**" vì máy của chúng tôi chỉ được trang bị **một ổ đĩa**: không có khả năng dự phòng để bảo vệ bộ nhớ tường lửa và dữ liệu của nó. Điều này đặc biệt quan trọng khi cài đặt trên máy vật lý để bảo vệ chống lại lỗi phần cứng của ổ đĩa, thông qua nguyên tắc RAID.



![Image](assets/fr/029.webp)



Ở bước thứ tư, chỉ cần nhấn **Enter** để xác nhận.



![Image](assets/fr/030.webp)



Cuối cùng, xác nhận bằng cách chọn "**YES**" rồi nhấn phím **Enter**.



![Image](assets/fr/031.webp)



Bây giờ bạn sẽ phải đợi trong khi OPNsense được cài đặt... Quá trình này mất khoảng 5 phút.



![Image](assets/fr/032.webp)



Sau khi cài đặt hoàn tất, chúng ta có thể đổi mật khẩu "**root**" trước khi khởi động lại. Chọn "**Root Password**", nhấn **Enter** và nhập mật khẩu "**root**" hai lần.



![Image](assets/fr/020.webp)



Cuối cùng, chọn "**Hoàn tất Cài đặt**" và nhấn **Enter**. Nhân cơ hội này, **đẩy đĩa ra khỏi ổ DVD của máy ảo**. Trong cài đặt máy ảo, bạn cũng có thể thiết lập khởi động đầu tiên vào đĩa.



![Image](assets/fr/021.webp)



Máy ảo sẽ khởi động lại và tải hệ thống OPNsense từ ổ đĩa, vì chúng ta vừa mới cài đặt nó. Đăng nhập bằng tài khoản "root" trong bảng điều khiển và mật khẩu mới của bạn (nếu không, mật khẩu mặc định là "**opnsense**").



### D. Liên kết các giao diện mạng



Màn hình hiển thị bên dưới sẽ xuất hiện. Chọn "**1**" và nhấn **Enter** để liên kết card mạng của máy với giao diện OPNsense.



![Image](assets/fr/022.webp)



Trước tiên, trình hướng dẫn sẽ yêu cầu bạn cấu hình liên kết tổng hợp và VLAN. Hãy nhập "**n**" để từ chối, và mỗi lần, hãy xác nhận câu trả lời bằng **Enter**. Tiếp theo, bạn cần gán hai giao diện "**hn0**" và "**hn1**" cho **WAN** và **LAN**. Về nguyên tắc, "**hn0**" tương ứng với WAN và Interface còn lại tương ứng với LAN.



Sau đây là cách thức hoạt động:



![Image](assets/fr/023.webp)



Bây giờ chúng ta có:





- **LAN** Interface được liên kết với card mạng "**hn1**" và với IP mặc định của OPNsense là Address, tức là **192.168.1.1/24**.
- Interface **WAN** được liên kết với card mạng "**hn0**" và với IP Address được truy xuất qua **DHCP** trên mạng cục bộ (nhờ bộ chuyển mạch ảo bên ngoài của chúng tôi).



Theo mặc định, việc quản trị OPNsense Interface chỉ có thể được truy cập từ mạng LAN Interface vì lý do bảo mật rõ ràng. Do đó, bạn phải kết nối với mạng LAN Interface của tường lửa để thực hiện quản trị. Nếu không thể, bạn có thể tạm thời quản trị OPNsense từ mạng WAN. Việc này bao gồm việc tắt chức năng tường lửa.



Để thực hiện việc này, hãy chuyển sang chế độ shell thông qua tùy chọn "**8**" và chạy lệnh sau:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Truy cập vào hệ thống quản lý OPNsense Interface



Có thể truy cập OPNsense Administration Interface qua HTTPS, sử dụng IP Address của LAN** Interface (hoặc WAN). Trình duyệt sẽ đưa bạn đến trang đăng nhập. Đăng nhập bằng tài khoản "root" và mật khẩu bạn đã chọn trước đó.



![Image](assets/fr/034.webp)



Đợi vài giây... Bạn sẽ được nhắc làm theo trình hướng dẫn để thực hiện cấu hình cơ bản. Nhấp vào "**Tiếp theo**" để tiếp tục.



![Image](assets/fr/036.webp)



Bước đầu tiên là xác định tên máy chủ, tên miền, chọn ngôn ngữ và xác định máy chủ DNS sẽ được sử dụng để phân giải tên. Việc giữ nguyên tùy chọn "**Enable Resolver**" sẽ cho phép tường lửa được sử dụng làm bộ phân giải DNS, điều này sẽ hữu ích cho các máy trong mạng LAN ảo của chúng ta.



![Image](assets/fr/037.webp)



Tiến hành bước tiếp theo. Trình hướng dẫn cung cấp cho bạn tùy chọn **xác định máy chủ NTP để đồng bộ hóa ngày và giờ**, mặc dù đã có máy chủ được cấu hình theo mặc định. Ngoài ra, điều quan trọng là phải chọn múi giờ tương ứng với vị trí địa lý của bạn (trừ khi bạn có yêu cầu đặc biệt).



![Image](assets/fr/038.webp)



Sau đó là một bước quan trọng: **cấu hình WAN Interface**. Hiện tại, nó được cấu hình trong DHCP và sẽ duy trì ở chế độ cấu hình này, trừ khi bạn muốn đặt IP tĩnh cho Address.



![Image](assets/fr/039.webp)



Vẫn trên trang cấu hình WAN của Interface, bạn cần bỏ chọn tùy chọn "**Chặn truy cập vào mạng riêng qua WAN**" nếu mạng ở phía WAN sử dụng địa chỉ riêng. Trường hợp này có thể xảy ra nếu bạn đang chạy Lab, và do đó có thể ngăn bạn truy cập Internet.



![Image](assets/fr/040.webp)



Tiếp theo, bạn có thể **định nghĩa mật khẩu "root"**, nhưng điều này là tùy chọn vì chúng ta đã thực hiện rồi.



![Image](assets/fr/041.webp)



Tiếp tục đến cuối để bắt đầu tải lại cấu hình. Nếu bạn cần tiếp tục kiểm soát qua WAN, hãy khởi động lại lệnh trên sau khi quá trình này hoàn tất.



![Image](assets/fr/042.webp)



Chỉ có vậy thôi!



![Image](assets/fr/035.webp)



### E. Cấu hình DHCP



Mục tiêu của chúng tôi là sử dụng máy chủ DHCP OPNsense để phân phối địa chỉ IP trên mạng LAN ảo. Để thực hiện việc này, chúng ta cần truy cập vào vị trí menu này:



```
Services > ISC DHCPv4 > [LAN]
```



**Như bạn thấy, DHCP đã được bật mặc định trên mạng LAN ** Nếu bạn không quan tâm đến dịch vụ này, bạn nên tắt nó. Mặc dù dịch vụ này đã được bật và chúng tôi muốn sử dụng, nhưng việc xem lại cấu hình của nó là rất quan trọng.



Nếu cần, bạn có thể thay đổi phạm vi địa chỉ IP được phân phối: **192.168.10.10** thành **192.168.10.245**, tùy thuộc vào cài đặt hiện tại.



![Image](assets/fr/046.webp)



Chúng ta cũng có thể thấy rằng các trường "**Máy chủ DNS**", "**Cổng**", "**Tên miền**", v.v., mặc định là trống. Trên thực tế, một số tùy chọn và giá trị mặc định nhất định cho các trường này được tự động kế thừa. Ví dụ: đối với máy chủ DNS, IP Address của mạng LAN Interface sẽ được phân phối, cho phép tường lửa OPNsense được sử dụng làm bộ phân giải DNS.



Lưu cấu hình sau khi thực hiện bất kỳ thay đổi nào, nếu cần.



![Image](assets/fr/047.webp)



Để kiểm tra máy chủ DHCP, bạn cần kết nối một máy với mạng LAN của tường lửa.



Máy này phải nhận được IP Address từ máy chủ DHCP của OPNsense, và máy của chúng tôi phải có quyền truy cập vào mạng. Truy cập Internet phải hoạt động. Xin lưu ý rằng nếu bạn đã tắt chức năng tường lửa để truy cập OPNsense từ WAN, điều này sẽ vô hiệu hóa NAT, ngăn bạn truy cập Web.



**Lưu ý**: các hợp đồng thuê DHCP hiện tại có thể được nhìn thấy từ Interface của chương trình quản trị OPNsense. Để thực hiện việc này, hãy truy cập vào vị trí sau: **Dịch vụ > ISC DHCPv4 > Hợp đồng thuê**.



![Image](assets/fr/045.webp)



### F. Cấu hình NAT và các quy tắc tường lửa



Tin tốt là bây giờ chúng ta có thể truy cập vào quản trị OPNsense Interface từ mạng LAN.



```
https://192.168.1.10
```



Sau khi đăng nhập vào OPNsense, hãy cùng khám phá cấu hình NAT. Truy cập vào đường dẫn này: **Tường lửa > NAT > Outbound**. Tại đây, bạn có thể chọn giữa việc tạo quy tắc NAT outbound tự động (mặc định) hoặc thủ công.



Chọn chế độ tự động thông qua tùy chọn "**Tự động tạo quy tắc NAT gửi đi**" và nhấp vào "**Lưu**" (về nguyên tắc, cấu hình này đã được kích hoạt). Ở chế độ tự động, OPNsense sẽ tự tạo một quy tắc NAT cho mỗi mạng của bạn.



![Image](assets/fr/043.webp)



Hiện tại, tất cả máy tính được kết nối với mạng LAN ảo "**192.168.10.0/24**" đều có thể truy cập Internet không hạn chế. Tuy nhiên, mục tiêu của chúng tôi là hạn chế quyền truy cập vào mạng WAN bằng các giao thức HTTP và HTTPS, cũng như DNS trên mạng LAN Interface của tường lửa.



Vì vậy, chúng ta cần tạo các quy tắc tường lửa... Duyệt menu như sau: **Tường lửa > Quy tắc > LAN**.



**Theo mặc định, có hai quy tắc để cấp phép cho tất cả lưu lượng LAN đi, trong IPv4 và IPv6**. Hãy hủy kích hoạt hai quy tắc này bằng cách nhấp vào mũi tên Green ở góc trái, đầu mỗi dòng.



Sau đó tạo ba quy tắc mới để cho phép **mạng LAN** (tức là "**mạng LAN**"):





- truy cập tất cả các đích đến bằng cách sử dụng **HTTP**.
- truy cập tất cả các đích đến bằng **HTTPS**.
- yêu cầu **OPNsense** trên **Interface LAN** (tức là "**LAN Address**"), thông qua **giao thức DNS** (điều này ngụ ý sử dụng tường lửa làm DNS), nếu không, hãy ủy quyền cho trình phân giải DNS của bạn thông qua IP Address.



Điều này đưa ra kết quả sau:



![Image](assets/fr/044.webp)



Việc còn lại là nhấp vào "**Áp dụng thay đổi**" để chuyển các quy tắc tường lửa mới sang môi trường sản xuất. **Xin lưu ý rằng tất cả các luồng không được ủy quyền rõ ràng sẽ bị chặn theo mặc định.



Máy LAN có thể truy cập Internet bằng HTTP và HTTPS. Tất cả các giao thức khác sẽ bị chặn.



![Image](assets/fr/018.webp)



## IV. Kết luận



Bằng cách làm theo hướng dẫn này, bạn sẽ có thể cài đặt OPNsense và bắt đầu sử dụng ngay lập tức. OPNsense cung cấp nhiều tính năng để bảo mật và quản lý lưu lượng mạng của bạn một cách hiệu quả, phù hợp để sử dụng trong môi trường chuyên nghiệp.



Cài đặt này chỉ là bước khởi đầu: bạn có thể thoải mái khám phá các menu và cấu hình các tính năng khác để điều chỉnh OPNsense theo nhu cầu của bạn.