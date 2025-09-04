---
name: Ntopng
description: Giám sát mạng của bạn với ntopng
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Florian Duchemin được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã có một số thay đổi.*



___



## I. Trình bày



**Cho dù là để kiểm tra tính lưu động của mạng, để có được bức tranh rõ ràng về mức sử dụng hay để thống kê hiệu suất, giám sát lưu lượng mạng là một phần quan trọng của mạng doanh nghiệp**. Nó giúp dự đoán những thay đổi đối với cơ sở hạ tầng và giúp đảm bảo chất lượng sử dụng cho người dùng (còn được gọi là QoE, viết tắt của *Chất lượng Trải nghiệm*, trái ngược với QoS).



Để thực hiện việc này, có nhiều kỹ thuật và phần mềm/giao thức khả dụng. Ví dụ, Netflow, do Cisco phát triển, có thể được sử dụng để truy xuất số liệu thống kê lưu lượng IP từ Interface, nhưng việc sử dụng nó bị giới hạn ở các thiết bị tương thích.



Đó là lý do tại sao trong hướng dẫn này tôi sẽ giới thiệu **Ntop** và chỉ cho bạn cách sử dụng nó trong cơ sở hạ tầng của bạn để theo dõi mức sử dụng mạng.



Ntop là phần mềm mã nguồn mở có thể cài đặt trên bất kỳ máy Linux nào. Phần mềm này hoàn toàn miễn phí và có thể thu thập các dữ liệu sau:





- Sử dụng băng thông
- Khách hàng chính
- Điểm đến chính
- Giao thức được sử dụng
- Ứng dụng được sử dụng
- Cổng được sử dụng
- Vân vân.



Hiện đã được đổi tên thành **Ntopng (Thế hệ mới)**, ứng dụng cung cấp nhiều chức năng cơ bản miễn phí. Phiên bản thương mại cũng có sẵn, cho phép xuất cảnh báo đã cấu hình sang phần mềm kiểu SIEM hoặc lọc lưu lượng truy cập bằng các quy tắc được xác định trực tiếp từ đầu dò.



## II. Điều kiện tiên quyết



Việc lắp đặt đầu dò Ntop khác nhau tùy theo thiết bị và môi trường. Vì vậy, tôi sẽ không hướng dẫn bạn từng bước ở đây, mà sẽ phác thảo các khả năng khác nhau.



### A. Chế độ trên bo mạch



Nếu bạn đang sử dụng tường lửa pfSense, OPNSense hoặc Endian, hoặc thậm chí là máy trạm Linux có NFTables, thì tin tốt đây! Bạn có thể cài đặt Ntopng trực tiếp và bắt đầu giám sát giao diện của mình.



Ưu điểm của kỹ thuật này là không yêu cầu phần cứng bổ sung. Mặt khác, nó làm tăng mức sử dụng tài nguyên, vì vậy hãy đảm bảo bạn có đủ phần cứng hoặc máy ảo (VM) có dung lượng đủ lớn (tối thiểu 2 lõi và 2GB RAM).



### B. Chế độ TAP / SPAN



**Tap** là **một thiết bị mạng có chức năng sao chép lưu lượng truyền qua nó và gửi đến một thiết bị khác.** Ưu điểm của thiết bị này là không yêu cầu bất kỳ sửa đổi nào đối với cơ sở hạ tầng hiện có và có thể được đặt ở bất kỳ đâu để giám sát các phần mạng cụ thể hoặc giữa bộ chuyển mạch lõi và bộ định tuyến biên để phân tích lưu lượng đến/đi từ Internet.



Nhược điểm lớn nhất của loại thiết bị này là chi phí. Trong mạng Gigabit hiện nay, một đầu thu thụ động không thể nắm bắt lưu lượng mạng một cách hiệu quả, vì vậy bạn cần một thiết bị chủ động có giá khoảng 200 euro (tối thiểu).



Chế độ **SPAN**, còn được gọi là **port mirroring**, được switch sử dụng để chuyển tiếp lưu lượng từ cổng này sang cổng khác. Đây là phương pháp tôi ưa thích nhất, vì nó dễ thiết lập và, giống như tap, cho phép bạn giám sát một phần hoặc toàn bộ mạng theo ý muốn. Tuy nhiên, có hai nhược điểm: switch phải tích hợp chức năng này, và việc sử dụng nó có thể làm tăng tải bộ xử lý trên switch.



### C. Chế độ bộ định tuyến



Hoàn toàn có thể cài đặt bộ định tuyến trên Linux và cài đặt ntopng. Nhược điểm duy nhất của phương pháp này là nó sẽ thay đổi địa chỉ mạng của bạn, hoặc địa chỉ nội bộ, hoặc địa chỉ giữa bộ định tuyến "thực" của bạn và bộ định tuyến bạn đang thêm vào.



Lưu ý: đối với độc giả của bài viết [Tạo bộ định tuyến Wifi bằng Raspberry Pi và RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/), bạn hoàn toàn có thể cài đặt ntopng trên Rpi của mình để có được số liệu thống kê chính xác!



### D. Chế độ cầu nối



Một giải pháp thay thế thú vị là sử dụng **một máy Linux ở chế độ cầu nối.** Được đặt giữa hai thiết bị, phương pháp này cho phép ghi lại toàn bộ lưu lượng mà không cần can thiệp vào cấu hình cơ sở hạ tầng hoặc thiết bị. Vì một máy tính cũ có thể làm được việc này, chi phí của phương pháp này cũng khá hấp dẫn. Lưu ý rằng để tối ưu, thiết bị nên có ba card mạng, hai card ở chế độ cầu nối, một card để truy cập Interface và SSH. Có thể chỉ sử dụng hai card, nhưng khi đó lưu lượng quản trị thiết bị cũng sẽ được ghi lại...



Vậy thì **đây là chế độ cuối cùng mà tôi sẽ sử dụng**. Vì lý do thực tế, tôi sẽ sử dụng máy ảo để trình diễn, nhưng phương pháp vẫn giữ nguyên khi sử dụng trên máy vật lý.



## III. Chuẩn bị đầu dò với cầu nối Interface



Đối với quá trình thăm dò, tôi chọn máy **Debian 11** ở chế độ cài đặt tối thiểu.



Bước đầu tiên, luôn giống nhau, cập nhật:



```
apt-get update && apt-get upgrade
```



Sau đó cài đặt gói **bridge-utils**, cho phép chúng ta tạo cầu nối:



```
apt-get install bridge-utils
```



Sau khi cài đặt, điều đầu tiên cần lưu ý là tên hiện tại của card mạng. Trên Debian, tên này có thể có nhiều dạng khác nhau và chúng ta sẽ cần nó để cấu hình.



Một lệnh **ip add** đơn giản sẽ trả về kết quả với thông tin sau:



![Image](assets/fr/016.webp)



Ở đây, tôi thấy 3 giao diện:





- Lo**: đây là Interface vòng lặp; nó là một Interface ảo "lặp vòng" qua thiết bị. Về cơ bản, Interface này, với Address là 127.0.0.1 (mặc dù bất kỳ Address nào trong 127.0.0.0/8 cũng được, vì dải này được dành riêng cho mục đích này) được sử dụng để kết nối với chính thiết bị. Nếu bạn đã cài đặt một trang web trên máy trạm (ví dụ: sử dụng WAMPP), có thể bạn đã từng sử dụng Address "*localhost*" để hiển thị trang web được lưu trữ trên máy của mình. Tên máy chủ này được liên kết với Address 127.0.0.1 và do đó với vòng lặp Interface.
- ens33**: đây là Interface đầu tiên của tôi, đã nhận được Address ở đây từ DHCP của tôi
- ens36**: Interface thứ hai của tôi



Bây giờ tôi đã có đầy đủ thông tin, tôi có thể chỉnh sửa tệp */etc/network/interfaces* để tạo cầu nối. Giao diện hiện tại của nó như sau (có thể khác):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Phần đầu tiên liên quan đến loopback Interface của tôi, mà tôi sẽ không động đến, tiếp theo là Interface ens33. Các sửa đổi bao gồm việc thêm Interface thứ hai (ens36) và cấu hình cầu nối với hai giao diện sau:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Sau đây là một số giải thích về những thay đổi đầu tiên này:





- auto *Interface***: sẽ tự động "khởi động" Interface khi khởi động hệ thống
- iface *Interface* hướng dẫn sử dụng inet**: sử dụng Interface mà không cần bất kỳ IP nào của Address. Giống như từ khóa "static" để định nghĩa IP tĩnh của Address hoặc "dhcp" để sử dụng địa chỉ động.



Các sửa đổi tiếp tục:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Một lần nữa, xin đưa ra một vài lời giải thích:





- iface br0 inet static**: ở đây tôi đã định nghĩa cầu nối Interface (*br0*) của mình bằng Address tĩnh.
- Address, mặt nạ mạng, cổng **: thông tin địa chỉ bo mạch
- bridge_ports**: các giao diện sẽ được đưa vào cầu nối
- bridge_stp**: Giao thức Spanning Tree được sử dụng khi kết nối các switch để phát hiện các liên kết dư thừa và tránh vòng lặp. Vì cầu nối có thể được chèn giữa hai đường dẫn mạng, nó có thể là nguồn gốc của vòng lặp, do đó có thể bật giao thức này. Tôi không cần nó ở đây, vì vậy tôi sẽ tắt nó.



Lưu các thay đổi và khởi động lại mạng:



```
systemctl restart networking
```



Để kiểm tra những thay đổi, hãy hiển thị lại kết quả của lệnh **ip** add:



![Image](assets/fr/021.webp)


Bạn có thể thấy rõ **Interface "*br0*" mới của tôi với IP Address mà tôi đã gán cho nó.** Nhân tiện, bạn cũng có thể thấy rằng hai giao diện vật lý của tôi thực sự "ĐANG HOẠT ĐỘNG", nhưng không có IP Address.



## IV. Cài đặt NtopNG



Bây giờ, khi trình thăm dò của chúng ta đã có thể đánh hơi lưu lượng giữa mạng của tôi và bộ định tuyến, tất cả những gì còn lại cần làm là cài đặt ntopng. Để thực hiện việc này, trước tiên hãy sửa đổi tệp */etc/apt/sources.list* và thêm **contrib** vào cuối mỗi dòng bắt đầu bằng **deb** hoặc **deb-src**.



Theo mặc định, nguồn gói chỉ chứa các gói tuân thủ DFSG (*Hướng dẫn Phần mềm Tự do Debian*), được xác định bằng từ khóa **main**. Bạn cũng có thể thêm các nguồn sau:





- contrib**: các gói chứa phần mềm tuân thủ DFSG, nhưng sử dụng các phần phụ thuộc không phải là một phần của nhánh **chính**
- không miễn phí**: chứa các gói không tuân thủ DFSG



Ví dụ về một dòng trong /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Vì vậy, tôi chỉ cần thêm từ **đóng góp** vào những dòng như thế này.



Các bước còn lại được liệt kê trên trang web [NtopNG] (https://packages.ntop.org/apt/), tại đó, đối với Debian 11, bạn cần thêm nguồn Ntop để cài đặt trong tương lai. Việc bổ sung này được tự động hóa bằng cách sử dụng lệnh:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Sau đó là giai đoạn cài đặt thực tế:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Lệnh đầu tiên xóa bộ nhớ đệm của trình quản lý gói apt. Lệnh thứ hai sẽ cập nhật danh sách gói và lệnh thứ ba sẽ cài đặt NtopNG.



Sau khi cài đặt, **phần mềm NtopNG sẽ có sẵn trực tiếp trên cổng 3000 của máy Debian**. Vì vậy, với tôi, đó là `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



Trang chủ NtopNG



Tên đăng nhập và mật khẩu mặc định sẽ được hiển thị, vì vậy bạn chỉ cần nhập chúng!



## V. Sử dụng NtopNG



Khi bạn đăng nhập lần đầu, điều đầu tiên bạn sẽ được yêu cầu làm là thay đổi mật khẩu quản trị viên mặc định và ngôn ngữ. Thật không may, tiếng Pháp không nằm trong số đó.



Sau đó, bạn sẽ thấy bảng điều khiển:



![Image](assets/fr/023.webp)



Bảng điều khiển NtopNG



Đừng quen với điều này! Nếu bạn để ý ô màu vàng ở đầu màn hình, bạn sẽ thấy dòng chữ: "*Giấy phép hết hạn sau 04:57*". Theo mặc định, quá trình cài đặt sẽ khởi chạy bản dùng thử phiên bản đầy đủ của NtopNG, nhưng trong thời gian (rất) giới hạn. Khi "thời gian đếm ngược" này kết thúc, phiên bản *cộng đồng* sẽ được kích hoạt và bảng điều khiển sẽ thay đổi:



![Image](assets/fr/024.webp)



Bảng điều khiển cộng đồng NtopNG mới



Điều đầu tiên cần làm là **kiểm tra xem Interface có đang nghe không**. Ở góc trên bên trái, danh sách thả xuống các giao diện khả dụng cho phép bạn chọn Interface mà chúng ta quan tâm tại đây: br0



![Image](assets/fr/025.webp)



Lựa chọn Interface



Cửa sổ mới hiển thị "Top Flaw Talkers", tức là các thiết bị giao tiếp nhiều nhất. Ở đây tôi chỉ thấy hai trạm xuất hiện:



![Image](assets/fr/026.webp)



**Máy chủ nguồn hiển thị bên trái, máy chủ đích hiển thị bên phải ** Điều này cho phép bạn hình dung tổng băng thông được sử dụng bởi mỗi máy chủ và có được cái nhìn tổng quan về lưu lượng mạng. Cũng không tệ, nhưng chúng ta có thể đi xa hơn...



Ví dụ, nếu tôi nhấp vào "*Máy chủ*", tôi sẽ thấy một biểu đồ hiển thị mức tiêu thụ điện năng gửi và nhận của từng máy chủ trong mạng. Ví dụ, ở đây tôi thấy chỉ riêng 192.168.1.37 đã chiếm tới 80% lưu lượng truy cập của tôi:



![Image](assets/fr/027.webp)



Nếu tôi nhấp vào IP Address của máy chủ đang đề cập, tôi sẽ được chuyển hướng đến trang tóm tắt:



![Image](assets/fr/028.webp)



Ví dụ, tôi có thể thấy rằng đó là máy VMWare (bằng cách nhận ra YES của máy MAC Address của tôi), rằng nó được gọi là DESKTOP-GHEBGV1 (chắc chắn là máy chủ Windows) VÀ tôi có **thống kê về các gói tin đã nhận và đã gửi, cũng như lượng dữ liệu**.



Bạn cũng sẽ thấy một menu mới ở đầu phần tóm tắt này. Tôi khuyên bạn nên nhấp vào "**Ứng dụng**" để xem điều gì đang thu hút nhiều lưu lượng truy cập đến vậy:



![Image](assets/fr/017.webp)


Ha, có vẻ như chúng ta đã có câu trả lời! Trên biểu đồ bên trái, **chúng ta thấy 76,6% lưu lượng truy cập đến từ ... Windows Update**, vậy là máy chủ này đang tải xuống các bản cập nhật!



NtopNG sử dụng công nghệ có tên DPI để *Kiểm tra gói tin sâu*, cho phép phân loại từng luồng mạng và xác định ứng dụng (hoặc họ ứng dụng) đằng sau nó.



Để minh họa, tôi chạy một video YouTube trên máy chủ của mình:



![Image](assets/fr/018.webp)



**Giao thông đã được nhận diện và phân loại ngay lập tức!



Lưu ý: vì những lý do hiển nhiên, loại phần mềm này có thể gây ra các vấn đề về quyền riêng tư, vì vậy hãy cẩn thận khi sử dụng trong điều kiện phù hợp. Cũng cần lưu ý rằng bạn có thể **ẩn danh kết quả**, tùy chọn này có thể được tìm thấy trong **Cài đặt > Tùy chọn > Khác** và được gọi là "**Mask Host IP Address**".



## VI. Phát hiện và cảnh báo



NtopNG cũng có khả năng đưa ra cảnh báo bảo mật trên một số nguồn cấp dữ liệu nhất định. Bạn có thể tìm thấy các cảnh báo này trong menu **Cảnh báo** ở biểu ngữ bên trái. Ví dụ, ở đây tôi có tổng cộng 2851 cảnh báo, được chia thành các mức độ nghiêm trọng khác nhau: Thông báo, Cảnh báo và Lỗi.



![Image](assets/fr/019.webp)



Hãy cùng xem qua các cảnh báo có mức độ nghiêm trọng cao, tôi có 17 cảnh báo như vậy!



Nhấp vào hình này sẽ hiển thị chi tiết cảnh báo. Không có gì đáng báo động ở đây, đây chỉ là báo động giả, việc tải xuống các bản cập nhật được phân loại là truyền tệp nhị phân trong luồng HTTP, điều này thực sự có thể đồng nghĩa với một cuộc tấn công.



![Image](assets/fr/020.webp)



Tuy nhiên, vì tôi đang sử dụng phiên bản miễn phí, tôi không thể loại trừ các tên miền hoặc máy chủ là nguồn cảnh báo, vì vậy bạn sẽ phải theo dõi chúng để tránh bỏ lỡ điều gì đó đáng lo ngại hơn nhiều. NtopNG sẽ cảnh báo generate trong trường hợp:





- Tải xuống tệp nhị phân qua HTTP
- Lưu lượng DNS đáng ngờ
- Sử dụng cổng không chuẩn
- Phát hiện tấn công SQL injection
- Tấn công xuyên trang web (XSS)
- Vân vân.



## VII. Kết luận



Trong hướng dẫn này, chúng ta đã thấy **cách thiết lập đầu dò với NtopNG** cho phép chúng ta **phân tích lưu lượng mạng** để trực quan hóa cách sử dụng giao thức và tình trạng chiếm dụng của từng máy chủ, đồng thời phát hiện lưu lượng đáng ngờ.



Thật không may, tôi không thể đề cập đến tất cả các tính năng và khả năng trong bài viết này, nhưng bạn cứ thoải mái khám phá nhé!



Giải pháp này có thể được triển khai lâu dài trong cơ sở hạ tầng doanh nghiệp. NtopNG cũng có thể xuất kết quả sang cơ sở dữ liệu InfluxDB, cho phép bạn tạo bảng thông tin riêng bằng công cụ của bên thứ ba như Graphana.