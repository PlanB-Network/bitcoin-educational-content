---
name: pfSense
description: Cài đặt Pfsense
---
![cover](assets/cover.webp)



___



*Bài hướng dẫn này dựa trên nội dung gốc của Florian BURNEL được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc của tác giả đã được chỉnh sửa đáng kể để cập nhật nội dung hướng dẫn.*



___



![Image](assets/fr/027.webp)



## I. Trình bày



pfSense là một hệ điều hành mã nguồn mở miễn phí, có khả năng biến bất kỳ máy tính, máy chủ chuyên dụng hoặc thiết bị phần cứng nào thành một bộ định tuyến và tường lửa hiệu suất cao, có khả năng cấu hình cao. Dựa trên FreeBSD và nổi tiếng với kiến trúc mạng ổn định, mạnh mẽ, pfSense đã thiết lập tiêu chuẩn cho tường lửa mã nguồn mở dành cho doanh nghiệp, chính quyền địa phương và người dùng gia đình khắt khe trong hơn mười lăm năm qua.



Các chức năng chính của pfSense đã phát triển đáng kể qua nhiều năm và được cải tiến qua mỗi phiên bản mới. Đến nay, pfSense cung cấp:





- Quản trị tập trung, hoàn chỉnh thông qua trang web Interface hiện đại, trực quan và an toàn.
- Tường lửa có trạng thái hiệu suất cao với hỗ trợ NAT nâng cao (bao gồm NAT-T) và quản lý quy tắc chi tiết.
- Hỗ trợ đa WAN gốc, cho phép tổng hợp hoặc dự phòng các kết nối Internet.
- Máy chủ DHCP và chuyển tiếp tích hợp.
- Tính khả dụng cao nhờ giao thức CARP để chuyển đổi dự phòng và khả năng cấu hình cụm pfSense.
- Cân bằng tải giữa nhiều kết nối hoặc máy chủ.
- Hỗ trợ VPN đầy đủ: IPsec, OpenVPN và WireGuard (thay thế L2TP, hiện đã lỗi thời).
- Cổng thông tin cố định có thể cấu hình để kiểm soát quyền truy cập của khách, đặc biệt là ở môi trường công cộng hoặc khách sạn.



pfSense còn có hệ thống gói mở rộng giúp dễ dàng thêm các tính năng nâng cao như proxy trong suốt (Squid), lọc URL hoặc IDS/IPS (Snort hoặc Suricata) trực tiếp từ web Interface.



pfSense chỉ được phân phối cho nền tảng 64-bit, phù hợp với khuyến nghị hiện hành của FreeBSD. Nó có thể được cài đặt trên phần cứng tiêu chuẩn (PC, máy chủ rack) hoặc trên các nền tảng nhúng công suất thấp như thiết bị Netgate hoặc một số hộp x86 cấu hình thấp, vốn mạnh hơn nhiều so với các hộp Alix cũ.



Cuối cùng, cần lưu ý rằng pfSense yêu cầu ít nhất hai giao diện mạng vật lý: một dành riêng cho vùng ngoài (WAN) và một dành riêng cho mạng nội bộ (LAN). Tùy thuộc vào độ phức tạp của cơ sở hạ tầng (DMZ, VLAN, nhiều WAN), có thể cần thêm một số giao diện bổ sung để tận dụng tối đa các tính năng của pfSense.



## II. Tải hình ảnh



Phiên bản ổn định mới nhất của pfSense, tại thời điểm viết hướng dẫn này, là 2.8 (phát hành vào tháng 6 năm 2025). Bạn có thể tải xuống ảnh ISO hoặc tệp cài đặt phù hợp với môi trường phần cứng của mình trực tiếp từ trang web chính thức:





- [Tải xuống pfSense](https://www.pfsense.org/download/)



Cổng tải xuống cho phép bạn lựa chọn:





- Kiến trúc (thường là **AMD64** cho tất cả phần cứng hiện đại).
- Loại hình ảnh (**Trình cài đặt USB Memstick** để cài đặt qua ổ USB, **Trình cài đặt ISO** để ghi hoặc chỉnh sửa ảo).
- Gương tải xuống gần nhất để tối ưu hóa tốc độ truyền tải.



Đối với những ai muốn triển khai pfSense trong môi trường ảo hóa (Proxmox, VMware ESXi, VirtualBox...), ảnh **OVA** cũng có sẵn. Máy ảo sẵn sàng sử dụng này giúp đơn giản hóa đáng kể việc cài đặt và cấu hình ban đầu. Chỉ cần đảm bảo bạn điều chỉnh các tài nguyên được phân bổ (CPU, RAM, giao diện mạng) theo tải dự kiến và cấu trúc mạng của bạn.



Trước khi cài đặt, chúng tôi khuyên bạn nên kiểm tra tính toàn vẹn của tệp đã tải xuống bằng cách xác minh **SHA256** được cung cấp trên trang tải xuống chính thức. Điều này đảm bảo rằng hình ảnh không bị thay đổi hoặc hỏng.



## III. Lắp đặt



Trong ví dụ này, quá trình cài đặt được thực hiện trên máy ảo chạy VirtualBox. Quy trình vẫn hoàn toàn giống nhau trên máy vật lý hoặc bất kỳ trình quản lý ảo hóa nào khác, ngoại trừ phần quản lý thiết bị ảo.



### 1. Yêu cầu phần cứng tối thiểu



Đối với việc triển khai tiêu chuẩn, chúng tôi khuyên bạn nên:





- Tối thiểu 1 GB RAM** (khuyến nghị 2 GB trở lên để hỗ trợ các gói bổ sung hoặc ZFS).
- Dung lượng đĩa 8 GB** (20 GB trở lên là lựa chọn tốt nhất cho các cấu hình nâng cao hơn, đặc biệt nếu bạn đang cài đặt bộ đệm proxy, IDS/IPS hoặc nhật ký chi tiết).
- Ít nhất hai giao diện mạng ảo** (một cho WAN, một cho LAN). Trong VirtualBox, hãy thêm chúng vào cài đặt VM trước khi khởi động.



### 2. Khởi động trình cài đặt



Mount ảnh ISO đã tải xuống dưới dạng ổ đĩa quang ảo trong VirtualBox hoặc cắm USB nếu bạn đang cài đặt trên máy thật. Khi khởi động, menu khởi động sẽ xuất hiện:



Nếu bạn không chọn bất kỳ tùy chọn nào, pfSense sẽ tự động khởi động với các tùy chọn mặc định sau vài giây. Nhấn phím "**Enter**" để bắt đầu khởi động bình thường.



![Image](assets/fr/027.webp)



Khi menu chính xuất hiện, hãy nhanh chóng nhấn nút "**I**" để bắt đầu cài đặt.



![Image](assets/fr/001.webp)



### 3. Cài đặt cài đặt ban đầu



Màn hình đầu tiên cho phép bạn thiết lập một số thông số khu vực, chẳng hạn như phông chữ hiển thị và mã hóa ký tự. Các thiết lập này hữu ích trong một số trường hợp cụ thể (bàn phím không chuẩn, màn hình nối tiếp, ngôn ngữ phương Đông). Đối với hầu hết các cài đặt, hãy giữ nguyên các giá trị mặc định và chọn "**Chấp nhận các Thiết lập này**".



![Image](assets/fr/002.webp)



### 4. Lựa chọn chế độ cài đặt



Chọn "**Cài đặt Nhanh/Dễ**" để chạy cài đặt tự động với các tùy chọn được đề xuất. Phương pháp này sẽ xóa ổ đĩa đã chọn và cấu hình pfSense với phân vùng mặc định.



![Image](assets/fr/003.webp)



Một cảnh báo sẽ xuất hiện, cho biết toàn bộ dữ liệu trên đĩa sẽ bị xóa. Xác nhận bằng "**OK**".



Trình cài đặt sau đó sẽ sao chép các tệp cần thiết vào ổ đĩa. Tùy thuộc vào phần cứng của bạn, quá trình này có thể mất từ vài giây đến vài phút.



### 5. Lựa chọn cốt lõi



Khi trình cài đặt nhắc bạn chọn loại kernel, hãy giữ nguyên tùy chọn "**Standard Kernel**". Kernel chung này hoàn toàn phù hợp với các triển khai tiêu chuẩn, dù trên PC, máy chủ hay VM.



### 6. Kết thúc cài đặt và khởi động lại



Sau khi cài đặt hoàn tất, hãy chọn "**Khởi động lại**" để khởi động lại máy trên phiên bản pfSense mới của bạn.



**Lưu ý quan trọng**: xóa ảnh ISO hoặc ngắt kết nối khóa USB cài đặt trước khi khởi động lại, để tránh phải khởi động lại chương trình cài đặt khi bạn khởi động lần sau.



## IV. Khởi động pfSense lần đầu tiên



Khi khởi động lần đầu, pfSense phải được cấu hình để nhận dạng và gán chính xác các giao diện mạng (WAN, LAN, DMZ, VLAN, v.v.). Việc xác định cẩn thận các card mạng là rất cần thiết để tránh bất kỳ lỗi cấu hình nào có thể khiến bạn không thể truy cập vào Interface web hoặc khiến tường lửa của bạn không hoạt động.



Khi khởi chạy, pfSense tự động phát hiện và liệt kê tất cả các giao diện mạng khả dụng, đồng thời chỉ ra địa chỉ MAC Address cho từng giao diện. Điều này giúp bạn dễ dàng phân biệt giữa chúng.



### 1. VLAN



Câu hỏi đầu tiên liên quan đến cấu hình VLAN. Ở giai đoạn này, đối với cấu hình cơ bản, chúng ta sẽ không kích hoạt bất kỳ VLAN nào. Vì vậy, hãy nhấn phím "**N**" để bỏ qua bước này.



![Image](assets/fr/004.webp)



### 2. WAN và LAN Interface Assignment



Sau đó, pfSense sẽ nhắc bạn xác định Interface nào sẽ được sử dụng cho WAN (truy cập Internet). Bạn có thể chọn giữa:





- Nhập tên Interface theo cách thủ công (khuyến nghị cho môi trường ảo).
- Sử dụng tính năng phát hiện tự động bằng cách nhấn "**A**". Tùy chọn này hữu ích trên máy chủ vật lý, miễn là cáp mạng của bạn đã được kết nối và các liên kết đang hoạt động.



![Image](assets/fr/005.webp)



Trong ví dụ này, chúng tôi sẽ cấu hình WAN theo cách thủ công. Nhập tên chính xác của Interface. Đối với bo mạch chủ Intel, tên thường là "**em0**" trong FreeBSD, nhưng có thể thay đổi tùy thuộc vào phần cứng. Ví dụ: card Realtek thường được hiển thị là "**re0**".



![Image](assets/fr/006.webp)



Lặp lại thao tác tương tự để xác định mạng LAN Interface. Ở đây, chúng tôi sử dụng "**em1**".



pfSense xác nhận rằng Interface LAN kích hoạt cả tường lửa và NAT để bảo vệ mạng nội bộ của bạn và quản lý quá trình chuyển đổi Address.



Nếu bạn có các giao diện vật lý khác, bạn có thể cấu hình thêm các giao diện khác (DMZ, Wi-Fi, VLAN cụ thể) ở giai đoạn này. Mỗi Interface logic yêu cầu một card mạng tương ứng hoặc Interface ảo. Đối với cấu hình ban đầu, chúng ta sẽ giới hạn ở WAN và LAN.



Sau khi hoàn tất việc phân công, pfSense sẽ hiển thị tóm tắt rõ ràng về sự tương ứng giữa các giao diện vật lý và các vai trò được phân công. Xác nhận bằng "**Y**".



### 3. Bảng điều khiển PfSense



Khi hoàn tất bước này, menu chính của bảng điều khiển pfSense sẽ xuất hiện. Nó cung cấp một số tùy chọn hữu ích cho việc quản trị trực tiếp, chẳng hạn như đặt lại mật khẩu web, khởi động lại, tải lại cấu hình hoặc gán lại giao diện.



![Image](assets/fr/007.webp)



Bạn cũng sẽ thấy tóm tắt về các thiết lập mạng hiện tại, bao gồm cả địa chỉ IP mặc định của Address trên mạng LAN Interface, thường là **192.168.1.1**. Đây là địa chỉ Address mà bạn cần nhập vào trình duyệt để truy cập trang quản trị Interface.



**Lưu ý**: Nếu mạng nội bộ của bạn sử dụng dải Address khác, hãy chọn "**2)** Đặt Interface(s) IP Address" trong menu để chỉ định IP Address phù hợp với môi trường của bạn.



Theo mặc định, nếu WAN Interface của bạn được kết nối với hộp hoặc modem được cấu hình DHCP, pfSense sẽ tự động lấy IP công cộng của Address. Do đó, bạn sẽ được hưởng lợi từ việc truy cập Internet ngay lập tức bằng cách kết nối máy khách với mạng LAN pfSense Interface.



## V. Lần đầu tiên truy cập vào trang web Interface



Sau khi quá trình khởi động ban đầu hoàn tất và giao diện mạng được cấu hình, bạn có thể truy cập trang web Interface của pfSense để hoàn thiện và tinh chỉnh cấu hình của mình.



### 1. Kết nối ban đầu



Kết nối máy tính với cổng LAN (hoặc mạng LAN Interface ảo trong trình quản lý ảo của bạn) và gán cho nó một địa chỉ IP Address trong cùng phạm vi nếu cần (theo mặc định, pfSense sẽ tự động phân phối Address qua DHCP trên mạng LAN).



Trong trình duyệt, hãy truy cập Address được chỉ định bởi bảng điều khiển (mặc định là `https://192.168.1.1`). Lưu ý rằng pfSense yêu cầu HTTPS ngay cả cho kết nối đầu tiên - vì vậy hãy chuẩn bị cảnh báo chứng chỉ tự ký, bạn có thể bỏ qua bằng cách thêm ngoại lệ.



Màn hình đăng nhập xuất hiện. Thông tin đăng nhập mặc định là:




- Tên người dùng:** `admin`
- Mật khẩu:** `pfsense`



Những mã định danh này sẽ được sửa đổi trong quá trình cấu hình ban đầu.



## VI. Trình hướng dẫn thiết lập



Khi kết nối lần đầu, pfSense sẽ nhắc bạn làm theo **Trình hướng dẫn Thiết lập**. Chúng tôi đặc biệt khuyến nghị bạn sử dụng trình hướng dẫn này để đảm bảo tất cả các thông số cần thiết được xác định chính xác.



### 1. Các thông số chung



Bạn có thể:




- Chỉ định tên máy chủ và tên miền cục bộ (ví dụ: `pfsense` và `lan.local`).
- Xác định máy chủ DNS và chọn xem pfSense có nên sử dụng DNS của ISP hay dịch vụ bên ngoài (Cloudflare, OpenDNS, Quad9...).



### 2. Múi giờ



Chỉ định múi giờ của trang web của bạn để nhật ký và lịch trình được nhất quán (ví dụ: `Châu Âu/Paris`).



### 3. Cấu hình WAN



Cấu hình kết nối WAN:




- Mặc định là **DHCP** (đủ nếu bạn đang sử dụng máy tính).
- Nếu bạn có IP cố định, hãy nhập các thông số (IP tĩnh, mặt nạ, cổng, DNS) theo cách thủ công.
- Nếu cần, hãy xác định xác thực VLAN hoặc PPPoE (phổ biến với một số ISP).



### 4. Cấu hình mạng LAN



Trình hướng dẫn đề xuất thay đổi mạng LAN mặc định. Nếu bạn đã có kế hoạch định địa chỉ cụ thể, hãy điều chỉnh ngay bây giờ.



### 5. Thay đổi mật khẩu quản trị viên



Bảo mật pfSense của bạn bằng cách thiết lập ngay mật khẩu mạnh cho người dùng `admin`.



## VII. Xác minh và cập nhật



Trước khi triển khai tường lửa, hãy đảm bảo bạn có phiên bản mới nhất của:





- Vào **Hệ thống > Cập nhật**.
- Chọn kênh cập nhật (thường là **Ổn định**).
- Kiểm tra bản cập nhật và áp dụng chúng.



Bạn nên bật thông báo cập nhật để luôn cập nhật được các bản vá bảo mật.



## VIII. Lưu cấu hình



Trước khi thực hiện bất kỳ thay đổi lớn nào, hãy triển khai chính sách sao lưu:





- Vào **Chẩn đoán > Sao lưu & Khôi phục**.
- Tải xuống bản sao cấu hình hiện tại (`config.xml`).
- Giữ nó ở nơi an toàn (phương tiện lưu trữ bên ngoài được mã hóa).



Đối với các môi trường quan trọng, hãy cân nhắc sao lưu cấu hình tự động trên máy chủ bên ngoài hoặc thông qua một tập lệnh được lập trình.



## IX. Thực hành tốt nhất sau khi cài đặt



Để kết thúc quá trình triển khai của bạn một cách an tâm:





- Sửa đổi quy tắc tường lửa**: theo mặc định, pfSense cho phép tất cả lưu lượng đi qua mạng LAN và chặn lưu lượng đến qua mạng WAN. Hãy điều chỉnh các quy tắc này nếu cần.
- Cấu hình truy cập từ xa an toàn**: nếu cần, chỉ cho phép truy cập vào web Interface từ WAN thông qua VPN hoặc với các hạn chế IP.
- Bật thông báo**: cấu hình máy chủ SMTP để nhận cảnh báo (lỗi, cập nhật, lỗi).
- Cài đặt các tiện ích mở rộng hữu ích**: ví dụ: IDS/IPS (Snort, Suricata), proxy (Squid), lọc DNS (pfBlockerNG).



Tường lửa pfSense của bạn hiện đã sẵn sàng hoạt động, sẵn sàng bảo vệ mạng. Nhờ tính linh hoạt và cộng đồng năng động, bạn có một công cụ mạnh mẽ, có khả năng mở rộng, có thể thích ứng với các nhu cầu trong tương lai (đa WAN, VLAN, VPN site-to-site, captive portal, v.v.).



Tham khảo tài liệu chính thức ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) thường xuyên để khám phá các tính năng mới và đảm bảo cấu hình của bạn được cập nhật và an toàn.