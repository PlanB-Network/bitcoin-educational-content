---
name: Lynis
description: Thực hiện kiểm tra bảo mật máy Linux bằng Lynis
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Fares CHELLOUG được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã được chỉnh sửa.*



___



## I. Trình bày



**Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách thực hiện kiểm tra bảo mật trên máy Linux bằng Lynis! Dành cho những ai chưa biết, **Lynis** là một tiện ích dòng lệnh nhỏ sẽ phân tích cấu hình máy chủ của bạn và đưa ra các đề xuất để **cải thiện bảo mật cho máy.**



Lynis là một công cụ mã nguồn mở của CISOFY, một công ty chuyên về **kiểm tra và củng cố hệ thống**. Nếu bạn muốn đạt được tiến bộ trong việc củng cố Linux và các dịch vụ phổ biến (SSH, Apache2, v.v.), Lynis chính là đồng minh của bạn! Lynis không chỉ cho bạn biết vấn đề đang gặp phải mà còn đưa ra các khuyến nghị giúp bạn đi đúng hướng (và tiết kiệm thời gian).



**Lynis** tương thích với hầu hết các bản phân phối Linux, bao gồm: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis hướng đến người dùng Linux/UNIX, nhưng cũng tương thích với **macOS**. Cài đặt rất nhanh, không có quản lý phụ thuộc ở cấp gói.



Nó được sử dụng cho nhiều mục đích khác nhau:





- Kiểm toán an toàn
- Kiểm tra sự tuân thủ (PCI, HIPAA và SOX)
- Cấu hình hệ thống khó khăn hơn
- Phát hiện lỗ hổng



Công cụ này được sử dụng rộng rãi bởi nhiều người dùng, bao gồm quản trị viên hệ thống, kiểm toán viên CNTT và chuyên gia kiểm thử thâm nhập. Về mặt phân tích, công cụ này dựa trên các tiêu chuẩn như **CIS Benchmark, NIST, NSA, OpenSCAP** và các khuyến nghị chính thức từ **Debian, Gentoo, Red Hat**.



Dự án có sẵn tại Address này trên **Github**:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Tải xuống Lynis từ CISOFY](https://cisofy.com/lynis/#download)



Trong hướng dẫn từng bước này, tôi sẽ **sử dụng VPS chạy Debian 12** và tôi sẽ tập trung vào phần SSH vì tôi muốn kiểm tra cấu hình của nó và cải thiện nó.



## II. Tải xuống và cài đặt



Có nhiều cách để tải xuống và cài đặt Lynis. Hãy chọn cách bạn thích nhất từ danh sách bên dưới.



### A. Cài đặt từ kho lưu trữ Debian



Chế độ cài đặt này cho phép bạn sử dụng lệnh **lynis** từ bất kỳ đâu trên hệ thống, không giống như cài đặt từ nguồn, nơi bạn cần phải ở trong thư mục.



Kết nối với máy chủ của bạn thông qua SSH và nhập các lệnh sau để cài đặt Lynis:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Đây là những gì bạn nhận được:



![Image](assets/fr/024.webp)



### B. Tải xuống từ trang web chính thức



Bạn cũng có thể tải xuống từ trang web Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Đây là những gì bạn nhận được:



![Image](assets/fr/032.webp)



Tiếp theo, chúng ta sẽ giải nén tệp lưu trữ bằng lệnh sau:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Đây là những gì bạn nhận được:



![Image](assets/fr/020.webp)



Chúng ta hãy chuyển đến thư mục **lynis**:



```
cd lynis
```



Chúng ta có thể kiểm tra các bản cập nhật bằng lệnh sau:



```
./lynis update info
```



Đây là những gì bạn nhận được:



![Image](assets/fr/023.webp)



### C. Tải xuống từ GitHub



Chúng ta sẽ tải xuống **Lynis** từ kho lưu trữ GitHub chính thức bằng lệnh sau (*git* phải có trên máy của bạn):



```
git clone https://github.com/CISOfy/lynis.git
```



Đây là những gì bạn nhận được:



![Image](assets/fr/060.webp)



## III. Sử dụng Lynis



Lynis có trên máy của chúng ta, vậy hãy cùng tìm hiểu cách sử dụng nó nhé!



### A. Các tùy chọn và điều khiển chính



Để hiển thị các lệnh có sẵn, chỉ cần nhập lệnh sau:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
./lynis
```



Đây là những gì bạn nhận được:



![Image](assets/fr/039.webp)



Và bạn cũng có được các tùy chọn sau:



![Image](assets/fr/040.webp)



Để hiển thị tất cả các lệnh có sẵn, hãy nhập lệnh sau:



```
sudo lynis show
```



Đây là những gì bạn nhận được:



![Image](assets/fr/022.webp)



Nếu bạn muốn hiển thị tất cả các tùy chọn, bạn phải nhập:



```
sudo lynis show options
```



Đây là những gì bạn nhận được:



![Image](assets/fr/021.webp)



Trong phần còn lại của bài viết này, chúng ta sẽ tìm hiểu cách sử dụng một số tùy chọn nhất định.



### B. Thực hiện kiểm toán hệ thống



Chúng ta sẽ yêu cầu **Lynis** kiểm tra hệ thống, đánh dấu những gì đã được cấu hình đúng và những gì cần cải thiện. Để thực hiện việc này, hãy nhập lệnh sau:



```
sudo lynis audit system
# ou
./lynis audit system
```



Theo mặc định, nếu bạn không đăng nhập với quyền root khi chạy lệnh này, công cụ sẽ chạy với quyền của người dùng hiện đang đăng nhập. Một số bài kiểm tra sẽ không được chạy trong ngữ cảnh này:



![Image](assets/fr/052.webp)



Sau đây là các bài kiểm tra sẽ không được thực hiện ở chế độ này:



![Image](assets/fr/051.webp)



Sau khi lệnh được thực thi, quá trình phân tích sẽ bắt đầu. Chỉ cần chờ một lát.



Khi kết thúc quá trình kiểm tra, bạn sẽ nhận được kết quả sau (chúng ta có thể thấy rằng **Lynis** đã xác định chính xác hệ thống **Debian 12** và sẽ sử dụng **phần bổ trợ Debian** để phân tích):



![Image](assets/fr/017.webp)



Tiếp theo, Lynis sẽ liệt kê một tập hợp các điểm tương ứng với mọi thứ anh ấy đã kiểm tra trên hệ thống của chúng tôi. Danh sách này được sắp xếp theo danh mục, như chúng ta sẽ thấy. Cũng cần lưu ý rằng mã màu được sử dụng để làm nổi bật các khuyến nghị:





- Đỏ** dành cho Elements quan trọng hoặc các biện pháp tốt nhất không được tôn trọng (ví dụ: gói bị thiếu), tức là máy chủ của bạn không tôn trọng điểm này
- Vàng** dành cho các đề xuất hoặc tuân thủ một phần khuyến nghị (giả sử việc tuân thủ một điểm được đánh dấu bằng màu này là một điểm cộng (không ưu tiên))
- Green** dành cho những điểm mà cấu hình máy chủ của bạn tuân thủ
- Trắng**, khi trung tính



Ở đây, chúng ta có thể thấy Lynis khuyên nên cài đặt **fail2ban**:



![Image](assets/fr/057.webp)



Trong phần "**Khởi động và dịch vụ**", chúng tôi thấy rằng việc bảo vệ dịch vụ thông qua *systemd* có thể được cải thiện. Về mặt tích cực, Grub2 đã có mặt và không có vấn đề gì về quyền trên:



![Image](assets/fr/029.webp)



Sau đó, bạn có các phần "**Kernel**" và "**Memory and Processes**":



![Image](assets/fr/037.webp)



Tiếp theo, phần "**Người dùng, Nhóm và Xác thực**". Công cụ sẽ thông báo cho chúng ta cảnh báo về quyền của thư mục "**/etc/sudoers.d**". Hiện tại, chúng tôi chưa biết thêm thông tin, nhưng chúng ta sẽ có thể xem khuyến nghị ở phần cuối của quá trình phân tích.



![Image](assets/fr/049.webp)



Sau đây là những thông tin bạn có thể tìm thấy trong các mục "**Shells", "Files Systems" và "USB Devices"**. Trong số những thông tin khác, chúng ta có thể thấy có các đề xuất về điểm gắn kết và các thiết bị USB hiện được phép sử dụng trên máy này.



![Image](assets/fr/048.webp)



Tiếp theo là các phần: "**Tên dịch vụ", "Cổng và gói", "Mạng".** Ở đây cho biết rằng các gói không còn được sử dụng có thể bị xóa và không có tiện ích nào có khả năng quản lý các bản cập nhật tự động.



![Image](assets/fr/058.webp)



Chúng ta có thể thấy tường lửa đã được kích hoạt (và vâng, còn có iptables nữa!). Ngoài ra, chúng ta có thể thấy tường lửa đã tìm thấy các quy tắc chưa sử dụng và máy chủ web Apache đã được cài đặt.



![Image](assets/fr/055.webp)



Tiếp theo là quá trình phân tích máy chủ web vì dịch vụ đã được xác định.



Chúng ta có thể thấy rằng nó đã tìm thấy các tệp cấu hình **Nginx**, và đối với phần SSL/TLS, các **mã hóa** được cấu hình bằng một giao thức không an toàn. Mặt khác, theo Lynis, việc quản lý nhật ký là chính xác.



![Image](assets/fr/038.webp)



Dịch vụ SSH hiện có trên máy chủ VPS của tôi. Cấu hình của nó được Lynis phân tích. Phải nói rằng bảo mật SSH có thể dễ dàng được cải thiện! Chúng tôi sẽ quay lại vấn đề này chi tiết hơn sau khi nhận được các khuyến nghị.



![Image](assets/fr/026.webp)



Sau đây là các phần **"Hỗ trợ SNMP", "Cơ sở dữ liệu", "PHP", "Hỗ trợ Squid", "Dịch vụ LDAP", "Ghi nhật ký và tệp"**.



Có một gợi ý thực sự quan trọng về quản lý nhật ký: chúng tôi đặc biệt khuyến nghị bạn không nên chỉ lưu trữ nhật ký cục bộ trên máy. Nếu máy bị tấn công, rất có thể kẻ tấn công sẽ cố gắng xóa dấu vết... Vì vậy, chúng ta cần lưu trữ nhật ký ra bên ngoài.



![Image](assets/fr/050.webp)



Tại đây, chúng ta có kiểm tra các dịch vụ dễ bị tấn công, quản lý tài khoản, tác vụ theo lịch trình và đồng bộ hóa NTP. Mức độ bảo mật được hiển thị ở mức thấp trên biểu ngữ và phần nhận dạng: điều này dễ hiểu, nếu bạn hiển thị phiên bản hệ thống, nó sẽ chỉ ra kẻ tấn công tiềm năng. Đây là cài đặt mặc định.



Sẽ rất thú vị nếu kích hoạt **auditd** để có nhật ký trong trường hợp phân tích **pháp lý**. **NTP** cũng được chọn, vì để tìm kiếm nhật ký hiệu quả, tốt nhất là nên có hệ thống hoạt động đúng giờ, giúp đơn giản hóa việc tìm kiếm.



![Image](assets/fr/036.webp)



Sau đó, Lynis xem xét Elements mã hóa, ảo hóa, container và các khuôn khổ bảo mật. Một số phần trống vì không có sự tương ứng với máy được phân tích. Tuy nhiên, chúng ta có thể thấy rằng tôi có hai chứng chỉ SSL đã hết hạn và tôi chưa kích hoạt **SELinux**.



![Image](assets/fr/027.webp)



Ở đây cũng có chỗ cần cải thiện: không có trình quét vi-rút hoặc phần mềm chống phần mềm độc hại và chúng tôi có đề xuất về quyền đối với tệp.



![Image](assets/fr/028.webp)



Tiếp theo, Lynis tập trung vào việc thắt chặt cấu hình hạt nhân Linux (bao gồm các quy tắc cho ngăn xếp IPv4) cũng như quản lý thư mục "Home" của máy Linux.



![Image](assets/fr/035.webp)



Chúng ta đã đi đến phần phân tích cuối cùng... Điểm cuối cùng này cho thấy chúng ta sẽ có được mọi lợi ích khi cài đặt ClamAV trên máy này.



![Image](assets/fr/030.webp)



## IV. Khuyến nghị



Sau khi kiểm tra, đã đến lúc đọc và phân tích các khuyến nghị. Đây là nơi chúng tôi nhận được các khuyến nghị và giải thích cho từng bài kiểm tra do Lynis thực hiện.



Lấy ví dụ về các khuyến nghị SSH. **Với mỗi đề xuất, bạn sẽ tìm thấy tham số được khuyến nghị và liên kết giải thích điểm bảo mật ** Tùy thuộc vào ngữ cảnh và cách sử dụng của bạn mà bạn có thể quyết định.



Chúng ta hãy cùng xem xét một số ví dụ về các khuyến nghị phản ánh trực tiếp các điểm được nêu bật trong suốt quá trình kiểm toán...



### A. Ví dụ về các khuyến nghị





- Như chúng ta đã thấy trước đó, NTP rất quan trọng đối với việc đóng dấu thời gian nhật ký:



![Image](assets/fr/043.webp)





- Lynis cũng gợi ý cài đặt gói **apt-listbugs** để có thông tin về các lỗi nghiêm trọng trong quá trình cài đặt gói thông qua **apt.**



![Image](assets/fr/041.webp)





- Công cụ này gợi ý chúng ta cài đặt **needrestart để có thể** xem tiến trình nào đang sử dụng phiên bản cũ của thư viện và cần khởi động lại.



![Image](assets/fr/054.webp)





- Gợi ý này đề xuất cài đặt **fail2ban** để tự động chặn các máy chủ không xác thực được (đặc biệt là tấn công bằng vũ lực).



![Image](assets/fr/044.webp)





- Để củng cố các dịch vụ hệ thống, ông khuyên chúng ta nên chạy lệnh màu xanh cho từng dịch vụ trên máy của mình.



![Image](assets/fr/056.webp)





- Ông đề xuất đặt ngày hết hạn cho tất cả mật khẩu tài khoản được bảo vệ.



![Image](assets/fr/031.webp)





- Gợi ý này đề xuất việc thiết lập giá trị tối thiểu và tối đa cho độ tuổi của mật khẩu. Điều này sẽ đảm bảo mật khẩu được thay đổi thường xuyên.



![Image](assets/fr/042.webp)





- Chúng tôi khuyên bạn nên sử dụng các phân vùng riêng biệt để hạn chế tác động của vấn đề về dung lượng đĩa trên một phân vùng.



![Image](assets/fr/047.webp)





- Khuyến nghị này đề xuất vô hiệu hóa bộ lưu trữ USB và firewire để ngăn chặn rò rỉ dữ liệu



![Image](assets/fr/033.webp)





- Để đáp ứng khuyến nghị này, chỉ cần cài đặt và cấu hình **unnated-upgrade** chẳng hạn.



![Image](assets/fr/053.webp)



### B. Cài đặt các gói được đề xuất



Để cải thiện cấu hình hệ thống, chúng ta sẽ cài đặt một số gói trên máy: một số do Lynis đề xuất, một số do cá nhân tôi đề xuất.



Bạn sẽ có một nền tảng tốt để làm việc, miễn là bạn dành một chút thời gian để cấu hình chúng. Để làm điều này, hãy tham khảo trang web IT-Connect, các bài viết khác trên Web và tài liệu hướng dẫn sử dụng công cụ.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Một số thông tin về các gói đã cài đặt:





- Clamav** là một phần mềm diệt virus.
- unattend-upgrades** sẽ cho phép bạn tự động quản lý các bản cập nhật và thậm chí khởi động lại máy hoặc tự động xóa các gói cũ, bạn có thể cấu hình đầy đủ.
- rkhunter** là một chương trình chống rootkit có chức năng quét hệ thống tập tin của bạn.
- Fail2ban** sẽ dựa trên các tệp nhật ký của bạn theo những gì bạn cung cấp cho nó để đọc và sẽ hoạt động với **iptables**, ví dụ như để cấm các địa chỉ IP cố gắng "tấn công thô bạo" máy chủ của bạn trong SSH.



### C. Khuyến nghị cho SSH



Hãy cùng xem qua các khuyến nghị về SSH được liệt kê bên dưới. Đừng lo lắng, chúng tôi sẽ giải thích ngay cách cải thiện cấu hình.



![Image](assets/fr/034.webp)



Chúng ta hãy xem xét kỹ hơn cấu hình **SSH** hiện tại của tôi trong :**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Cấu hình được đề xuất bên dưới vẫn có thể được tối ưu hóa, nhưng vẫn cung cấp cho bạn một nền tảng tốt. *Xin lưu ý rằng tôi đã xóa một số bình luận để dễ đọc hơn*.



Chúng tôi sẽ:





- Thay đổi cổng kết nối SSH (quên cổng mặc định 22)
- Tăng mức độ chi tiết của nhật ký, từ **INFO lên VERBOSE**
- Đặt **LoginGraceTime** thành **2 phút**



Nếu không nhập thông tin kết nối trong vòng hai phút, kết nối sẽ bị ngắt.





- Kích hoạt **strictModes**



Chỉ định liệu "sshd" có nên kiểm tra chế độ và chủ sở hữu của các tệp của người dùng cũng như thư mục home của người dùng trước khi xác thực kết nối hay không. Điều này thường được khuyến khích, vì đôi khi người dùng mới vô tình để thư mục hoặc tệp của họ được truy cập hoàn toàn bởi tất cả mọi người. Mặc định là "có".





- Đặt **MaxAuthtries** thành 3



Số liệu này biểu thị số lần xác thực không thành công trước khi giao tiếp kết thúc.





- Đặt **MaxSessions** thành 2



Con số này thể hiện số lượng phiên hoạt động đồng thời tối đa.





- Bật xác thực khóa công khai



```
PubkeyAuthentication yes
```





- Giữ lại xác thực mật khẩu:



```
PasswordAuthentication yes
```



Cấm mật khẩu trống và xác thực **Kerberos** cũng như **xác thực gốc trực tiếp**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Hãy đảm bảo rằng bạn có "**PermitRootLogin no", nếu bằng "yes" thì đó là "absolute evil"**.





- Cấm chuyển hướng kết nối TCP



```
AllowTcpForwarding no
```



Cho biết liệu chuyển hướng TCP có được phép hay không, với cài đặt mặc định là "có". Lưu ý: việc tắt chuyển hướng TCP không tăng cường bảo mật nếu người dùng có quyền truy cập vào shell, vì họ vẫn có thể thiết lập các công cụ chuyển hướng của riêng mình.





- Cấm chuyển hướng X11



```
X11Forwarding no
```



Cho biết liệu chuyển hướng X11 có được chấp nhận hay không, với cài đặt mặc định là "không". Lưu ý: ngay cả khi chuyển hướng X11 bị tắt, điều này cũng không làm tăng tính bảo mật, vì người dùng vẫn có thể thiết lập chuyển hướng riêng. Chuyển hướng X11 sẽ tự động bị tắt nếu chọn **UseLogin**.





- Đặt thời gian chờ giao tiếp giữa máy khách và sshd



```
ClientAliveInterval  300
```



Xác định thời gian chờ tính bằng giây. Sau thời gian này, nếu không nhận được dữ liệu từ máy khách, dịch vụ sshd sẽ gửi tin nhắn yêu cầu phản hồi từ máy khách. Theo mặc định, tùy chọn này được đặt thành "0", nghĩa là những tin nhắn này sẽ không được gửi đến máy khách. Chỉ phiên bản 2 của giao thức SSH mới hỗ trợ tùy chọn này.



```
ClientAliveCountMax 0
```



Theo [tài liệu (*trang hướng dẫn*) cho sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), tùy chọn này có nghĩa là: "Đặt số lượng tin nhắn giữ (xem ở trên) được gửi mà không cần phản hồi từ máy khách cho **sshd**. Nếu đạt đến ngưỡng này trong khi tin nhắn giữ đã được gửi, **sshd** sẽ ngắt kết nối máy khách và chấm dứt phiên. Điều quan trọng cần lưu ý là các tin nhắn giữ này rất khác so với tùy chọn **KeepAlive** (bên dưới). Tin nhắn giữ kết nối được gửi qua đường hầm được mã hóa và do đó không thể làm giả. Tính năng giữ kết nối ở cấp độ TCP được bật bởi **KeepAlive** có thể làm giả. Cơ chế giữ kết nối rất hữu ích khi máy khách hoặc máy chủ cần biết liệu kết nối có đang ở trạng thái nhàn rỗi hay không."





- Ngăn chặn việc tiết lộ thông tin bằng cách vô hiệu hóa **motd, banner, lastlog**



```
PrintMotd no
```



Chỉ định liệu sshd có nên hiển thị nội dung của tệp "/etc/motd" khi người dùng đăng nhập ở chế độ tương tác hay không. Trên một số hệ thống, nội dung này cũng có thể được hiển thị bởi shell, thông qua /etc/profile hoặc một tệp tương tự. Giá trị mặc định là "có".



```
Banner none
```



Cần lưu ý rằng ở một số khu vực pháp lý, việc gửi tin nhắn trước khi xác thực có thể là điều kiện tiên quyết để được bảo vệ pháp lý. Nội dung của tệp được chỉ định sẽ được truyền đến người dùng từ xa trước khi cấp quyền kết nối. Tùy chọn này cần được cấu hình, vì theo mặc định, sẽ không có tin nhắn nào được hiển thị.



Trong hình ảnh, điều này đưa ra:



![Image](assets/fr/019.webp)



### D. Điểm kiểm toán



Cuối cùng, đừng quên kiểm tra **điểm kiểm tra Lynis**! Chúng ta thấy **điểm Hardening của tôi là 63** và tệp báo cáo có thể được xem trong "**/var/log/lynis-report.dat**". Ngoài ra còn có tệp "**/var/log/lynis.log**".



**Nói cách khác, điểm càng cao càng tốt! Do đó, bạn cần cải thiện cấu hình để đạt được điểm cao nhất có thể, đồng thời cho phép máy tính và các dịch vụ được lưu trữ hoạt động bình thường (có nghĩa là thực hiện các bài kiểm tra chức năng).



![Image](assets/fr/046.webp)



Hãy cùng xem kết quả trên máy chủ thứ hai của tôi, nơi tôi đã dành nhiều thời gian hơn để "củng cố"! Vì vậy, điểm số cao hơn (**76**) là điều bình thường.



![Image](assets/fr/045.webp)



## V. Lynis tự động lập kế hoạch



**Lynis** cũng cung cấp tùy chọn chạy kiểm tra thông qua một tác vụ được lên lịch. Thực tế, có tùy chọn **"--cronjob "**, tùy chọn này sẽ chạy tất cả các bài kiểm tra Lynis mà không cần xác thực hoặc thao tác của người dùng. Sau đó, bạn có thể dễ dàng tạo một tập lệnh để chạy **Lynis** và lưu kết quả đầu ra vào một tệp có dấu thời gian với tên của máy chủ đang được đề cập. Dưới đây là một tệp thuộc loại này mà bạn có thể đặt trong thư mục */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



Biến **"AUDITOR_NAME "** chỉ đơn giản là một biến mà chúng ta sẽ đặt trong tùy chọn **"--auditor "** của **Lynis** để tên này được hiển thị trong báo cáo:



![Image](assets/fr/059.webp)



Chúng ta cũng sẽ tạo một số biến ngữ cảnh giúp chúng ta tổ chức tốt hơn, chẳng hạn như tên máy chủ và ngày đặt tên báo cáo và đóng dấu thời gian, cũng như đường dẫn đến thư mục mà chúng ta muốn lưu báo cáo.



## VI. Kết luận



Lynis là một công cụ rất thiết thực, giúp bạn tiết kiệm thời gian và làm việc hiệu quả hơn khi muốn tìm hiểu thêm về trạng thái cấu hình của máy chủ Linux, đặc biệt là về mặt bảo mật. Tuy nhiên, đừng quên rằng mọi sửa đổi đều phải được kiểm tra trước khi áp dụng vào thực tế, tùy thuộc vào cách sử dụng và bối cảnh của bạn.



Có lẽ bạn sẽ không áp dụng cùng một cấu hình cho VPS được kết nối với Net, nơi bạn chỉ cần một kết nối SSH (vì bạn là người duy nhất kết nối), không giống như **bastion** hoặc **scheduler** sẽ cần phải nhân các kết nối **SSH.**



Khi đã có cấu hình phù hợp về mặt bảo mật, bạn nên sử dụng một công cụ tự động hóa để không phải thực hiện lại các tác vụ theo cách thủ công, vì việc này sẽ tốn thời gian và dễ xảy ra lỗi. Ví dụ: bạn có thể sử dụng **: Puppet, Chef, Ansible, v.v...**



Đừng quên trao đổi với nhóm của bạn trước khi triển khai: bạn cần giúp họ hiểu lý do tại sao bạn thực hiện những thay đổi này, chứ không chỉ nói suông. Mục đích cuối cùng là truyền đạt những thực hành tốt, và điều này sẽ tăng cơ hội thành công của bạn.



Cuối cùng, bạn cũng có thể so sánh **Lynis** với các công cụ khác, hiện có rất nhiều. Nếu bạn muốn chuyển sang quản lý tập trung mà vẫn giữ được tính mở, tôi khuyên bạn nên sử dụng công cụ [Wazuh] (https://wazuh.com/).



**Hướng dẫn này đã kết thúc, hãy vui vẻ cùng Lynis nhé!