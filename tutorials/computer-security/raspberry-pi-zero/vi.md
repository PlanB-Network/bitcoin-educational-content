---
name: Raspberry Pi Zero
description: Cách xây dựng một máy tính tối giản, cách ly và chi phí thấp bằng Raspberry Pi Zero và bộ phụ kiện.
---
![cover](assets/cover.webp)



Nếu bạn đã theo dõi trang Plan ₿ Network một thời gian, bạn hẳn đã biết rằng một trong những thiết lập bảo mật được ủng hộ nhiều nhất, gần như là bắt buộc, **là quản lý tiền bằng cách lưu trữ ngoại tuyến khóa riêng tư của bạn**.



Nếu bạn chưa khám phá ra điều này, trong suốt hướng dẫn này, bạn sẽ tìm thấy các liên kết đến các tài nguyên nguồn mở để tìm hiểu thêm về nó.



Để quản lý khóa riêng ngoại tuyến, cần có một thiết bị luôn được ngắt kết nối khỏi mạng, có thể là [ví phần cứng](https://planb.network/resources/glossary/hardware-wallet) hoặc máy tính airgap, được dành riêng cho chức năng cụ thể này.



Bạn sẽ làm thế nào nếu chẳng hạn, bạn không có khả năng mua phần cứng chỉ thực hiện nhiệm vụ này, nhưng bạn lại không muốn từ bỏ bước bảo mật này?



## Giải pháp


Nếu tôi nói với bạn rằng bạn có thể tạo ra một thiết bị ngoại tuyến dưới dạng máy tính airgap có kích thước và trọng lượng chỉ bằng một ổ đĩa flash USB và giá chỉ 35 euro thì sao? Bạn có tin không?



Tiếp tục đọc.



Tôi sẽ nói thêm với bạn: hãy đọc hết. Giải pháp được đề xuất tuy rẻ, nhưng không hẳn là dễ nhất. Trước tiên, bạn cần nắm được ý chính, sau đó quyết định dành thời gian nghiên cứu cá nhân và lựa chọn, với sự an tâm tối đa, liệu có nên tiếp tục hay không và tiếp tục như thế nào.



## Yêu cầu


**1** Một [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (không có bất kỳ hậu tố nào) là nền tảng để xây dựng một máy tính với hiệu năng tối thiểu, nhưng quan trọng hơn cả là nó thiếu thẻ Wi-Fi và Bluetooth, những yêu cầu thiết yếu cho mục đích của bài tập này.





- Chi phí**: khoảng 15,00 tại thời điểm viết hướng dẫn này (tháng 8 năm 2025).
- Tính liên tục của sản xuất**: Raspberry đảm bảo sản xuất đến tháng 1 năm 2030.



Rất tiếc, PI Zero không có Wi-Fi và Bluetooth, hiện đã gần như không còn khả dụng. Bạn có thể tìm các lựa chọn thay thế cho PI Zero W và PI Zero 2W dễ dàng hơn. Trong trường hợp này, bạn có thể tắt chức năng kết nối bằng cách thay đổi tệp cấu hình. Sau khi cài đặt hệ điều hành, bạn sẽ cần thêm các mục sau vào tệp cấu hình:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



Một phần của hướng dẫn này sẽ chỉ cho bạn cách thực hiện và nơi thực hiện. Tuy nhiên, nếu bạn thực sự muốn chắc chắn, bạn có thể tìm thấy một số hướng dẫn trên web về cách tháo chip Wi-Fi bằng dao cắt nhỏ, loại dao phù hợp để làm việc trên bo mạch điện tử.



**2** Một _bộ khởi động_ cho Raspberry PI Zero: giống như thông lệ của thế giới Raspberry, chỉ có phần khung, không có vỏ ngoài. Hơn nữa, nguồn tài nguyên hạn chế của một bo mạch nhỏ như vậy cũng hạn chế khả năng kết nối với thế giới bên ngoài.



Khi quyết định tiếp tục, tôi tìm thấy [bộ sản phẩm này](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) đầy đủ phụ kiện, giúp tận dụng tối đa tiềm năng của PI Zero. Bộ sản phẩm bao gồm một bộ chuyển đổi USB A -> micro USB Supply, một hub USB nhỏ, một bộ chuyển đổi mini-HDMI -> HDMI, một tản nhiệt bằng đồng và một vỏ ngoài bằng nhôm. Bộ sản phẩm cũng bao gồm các ốc vít và cờ lê lục giác cần thiết để lắp PI Zero vào vỏ mới.





- Giá**: 19,99 euro.



**3** Hướng dẫn này không yêu cầu bạn phải chi tiêu quá nhiều tiền cho máy tính airgap. Tuy nhiên, bạn nên biết rằng bạn sẽ cần một bàn phím và chuột USB (cần phải có dây, tránh Bluetooth) và một màn hình. Tùy thuộc vào đầu vào màn hình, bạn có thể cần một bộ chuyển đổi từ mini-HDMI, cổng ra duy nhất có sẵn trên PI Zero. Cuối cùng, hãy xem Hard để biết rằng tất cả chúng ta đều có bàn phím và chuột không dây ở đâu đó trong nhà - đã đến lúc Dust tháo chúng ra.



## Ngân sách bổ sung



**4** Bạn có thể mua bộ nguồn Supply gốc từ Raspberry với giá khoảng 15,00 euro.



**5** Cá nhân tôi đã chọn sử dụng nguồn điện Supply được cung cấp trong _bộ khởi động_, tuy nhiên, kết hợp nó với cáp USBA → miniUSB được gọi là `không có dữ liệu`, có giá 3,70 euro.



**6** Thẻ nhớ micro SD, có dung lượng lưu trữ tối thiểu là 32 GB; nếu chất lượng/mức độ công nghiệp tốt hơn.



**7** Bạn sẽ cần một hệ thống, một bộ chuyển đổi USB sang micro SD, như cái bạn thấy trong hình. Hệ điều hành và bộ nhớ của PI Zero sẽ hoạt động trên phương tiện đó.



![img](assets/it/06.webp)



## Cài đặt hệ điều hành


Trước khi đóng PI Zero vào vỏ máy, tôi khuyên bạn nên cài đặt hệ điều hành. Sau đó, bạn sẽ có thể kiểm tra đèn LED báo hiệu hoạt động ngay lập tức.



Để chọn và ghi hệ điều hành, tôi đã chọn cách dễ nhất: sử dụng công cụ `PI Imager` của Raspberry.



![img](assets/it/01.webp)



Hãy truy cập [Github của Raspberry](https://github.com/raspberrypi/rpi-imager/releases) để tải về bản phát hành mới nhất của Imager, chọn phiên bản phù hợp nhất với hệ điều hành của bạn (v. 1.9.6 tại thời điểm viết). Bạn sẽ nhận thấy rằng bên cạnh mỗi tệp còn có mã băm của tệp tương ứng. Điều này sẽ hữu ích cho việc xác minh.



![img](assets/it/02.webp)



Tôi khuyên bạn nên kiểm tra hệ điều hành bạn sẽ sử dụng trên máy tính airgap để đảm bảo an toàn. Điều này sẽ giúp bạn yên tâm rằng mình đang sử dụng phiên bản Imager hợp pháp (không độc hại) và do đó, là Raspi OS.



Thực hiện xác minh ngay sau khi tải xuống, với máy bạn thường sử dụng được kết nối Internet



Sau đó, mở terminal Linux và chuẩn bị tải xuống, tạo thư mục `raspios` hữu ích để làm việc.



![img](assets/it/19.webp)



Tải xuống Imager cho bản phân phối Linux của bạn bằng `wget`.



![img](assets/it/20.webp)



Cuối cùng, hãy chạy lệnh `sha256sum` và so sánh Hash với lệnh do Raspberry cung cấp trên Github.



![img](assets/it/21.webp)



Hoặc, nếu bạn dùng Windows, hãy mở Power Shell và nhập lệnh sau:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Bạn sẽ nhận được Hash phải trùng khớp với phiên bản đã công bố trên Raspberry Github.



Sau khi xác minh tải xuống, bạn có thể cài đặt Imager trên máy tính thường dùng và mở nó. Imager là công cụ bạn cần để ghi hệ điều hành vào thẻ nhớ micro SD, đây sẽ là "đĩa hệ thống" của PI Zero.



Quá trình này cực kỳ đơn giản: trước tiên hãy chọn thiết bị Raspberry mà bạn sẽ sử dụng (vì vậy hãy chú ý đến **mẫu** Raspi Zero của bạn), sau đó là phiên bản hệ điều hành và cuối cùng là điểm gắn thẻ micro SD để flash hệ điều hành.



### Bước đầu tiên



![img](assets/it/03.webp)



### Bước thứ hai



![img](assets/it/07.webp)



**Lưu ý**: chọn `PI OS 32-bit`, phiên bản duy nhất hoạt động với PI Zero.



### Bước thứ ba



![img](assets/it/08.webp)



(Hãy cẩn thận khi chọn _Loại trừ ổ đĩa hệ thống_ để tránh bị nhắc cài đặt hệ điều hành Raspi trên máy tính của bạn.)



Khi mọi thứ đã được thiết lập xong, Imager sẽ hỏi bạn có muốn sử dụng cài đặt tùy chỉnh hay không. Hãy chọn cài đặt bạn muốn hoặc nhấp vào _Không_ để tiếp tục với các tùy chọn mặc định.



![img](assets/it/09.webp)



Xác nhận rằng bạn muốn xóa nội dung của thẻ nhớ micro SD



![img](assets/it/10.webp)



Thiết bị Imager bắt đầu nạp hệ điều hành vào thẻ nhớ micro SD, thanh cuộn sẽ thông báo cho bạn về tiến trình.



![img](assets/it/11.webp)



Cuối cùng sẽ có xác minh tự động, tôi khuyên bạn không nên dừng lại.



![img](assets/it/12.webp)



Cuối cùng, một thông báo sẽ xuất hiện trên màn hình và nếu mọi thứ thành công, nó sẽ trông giống như những gì bạn đọc trong hình.



![img](assets/it/13.webp)



Bây giờ bạn có thể thực sự tháo thẻ micro SD khỏi đầu đọc và đặt nó vào khe của PI Zero. Bật Raspberry nhỏ và quan sát đèn LED: chúng tôi mong đợi nó có màu xanh lá cây và nhấp nháy, cho thấy hệ điều hành đang được tải bình thường, sau đó sẽ sáng liên tục. Nếu bạn thấy dấu hiệu khác, ví dụ như đèn LED nhấp nháy với tần số đều đặn hoặc có màu đỏ, hãy tham khảo FAQ hoặc [các trang diễn đàn hỗ trợ](https://forums.raspberrypi.com/).



## Cấu hình đầu tiên


Lần khởi động đầu tiên của Raspi OS sẽ chậm hơn bình thường một chút vì phải thực hiện một số tác vụ cài đặt thực tế. Tuy nhiên, nếu mọi việc suôn sẻ, bạn sẽ thấy màn hình chào mừng.



![img](assets/it/14.webp)



Nhấp vào _Tiếp theo_ để thiết lập khu vực địa lý, đặc biệt là để tải đúng bàn phím. Hãy đặc biệt chú ý đến phần sau.



![img](assets/it/15.webp)



Nhấp vào _Tiếp theo_ và bạn sẽ được yêu cầu tạo người dùng, ghi lại thông tin đăng nhập và lưu giữ chúng cẩn thận.



![img](assets/it/16.webp)



Trình hướng dẫn sẽ yêu cầu bạn chọn trình duyệt web mặc định, giữa Chromium và Firefox; trình hướng dẫn cũng có thể hỏi bạn về cài đặt mạng Wi-Fi nếu bạn đang sử dụng PI Zero W hoặc 2W. Hãy nhấp vào _Bỏ qua_.



Đến một lúc nào đó, bạn sẽ được nhắc nâng cấp phần mềm và hệ điều hành tích hợp. Chọn _Bỏ qua_: vì mục đích của bài tập này, thực tế chúng ta đang xây dựng một máy tính ngoại tuyến, và máy tính này phải duy trì trạng thái ngoại tuyến tại thời điểm này.



Cuối cùng, nó có thể yêu cầu bạn bật `ssh`, nhưng hãy từ chối bước này vì đây là IP không có khoảng cách không khí.



![img](assets/it/17.webp)



Không cần cấu hình thêm gì nữa. Khi hoàn tất, hãy khởi động lại Raspberry để những thay đổi có hiệu lực.



![img](assets/it/18.webp)



## Một khoảng cách không khí máy tính mới


Sau khi khởi động lại, máy tính airgap mới của bạn đã sẵn sàng. PI Zero sẽ hiển thị màn hình nền mới, bạn có thể sử dụng thông qua GUI hoặc từ dòng lệnh.



![img](assets/it/22.webp)



### Những bước đầu tiên cho PI Zero W hoặc 2W


Nếu bạn đang sử dụng Raspberry PI Zero W hoặc dòng 2W, bo mạch của bạn đã được tích hợp sẵn chip Wi-Fi và Bluetooth. Trong lần thiết lập đầu tiên, bạn đã bỏ qua bước cấu hình kết nối, do đó PI Zero không được kết nối Internet. Giờ đây, bạn có thể tắt vĩnh viễn hai chip này bằng phần mềm.



Trên thực tế, Raspi OS cung cấp một tệp `config.txt` mà bạn có thể chỉnh sửa theo ý thích. Tệp `config` nằm trong phân vùng `boot`, trong thư mục `firmware`, và bạn có thể chỉnh sửa và lưu tệp này với quyền `root`.



Mở terminal từ biểu tượng ở góc trên bên trái và nó sẽ trở thành `root`.(1)



![img](assets/it/23.webp)



(1) Nếu hệ điều hành Raspi không yêu cầu bạn tạo mật khẩu `root` trong các bước trước, tôi khuyên bạn nên thực hiện ngay bây giờ bằng lệnh `passwd`. Việc di chuyển người dùng `root` độc lập với người dùng cá nhân của bạn có thể rất tiện lợi trong các tình huống khôi phục.



Với thiết bị đầu cuối, hãy kiểm tra tệp `config.txt` và chuẩn bị chỉnh sửa tệp này bằng trình soạn thảo `nano`.



![img](assets/it/24.webp)



Việc chỉnh sửa nên được thực hiện ở cuối toàn bộ `config`, sau dòng chữ `[All]`. Tại thời điểm này, bạn sẽ thêm các lệnh `dtoverlay` được hiển thị ở đầu hướng dẫn.



![img](assets/it/25.webp)



Lưu, đóng và khởi động lại. Ở bước tiếp theo, chúng ta sẽ khám phá Raspberry nhỏ.



## Có thể mong đợi gì ở thiết bị này?


Xem [thông số kỹ thuật](https://www.raspberrypi.com/products/raspberry-pi-zero/) trên trang web của Raspberry, PI Zero có bộ xử lý BCM2835 lõi đơn và RAM 512 MB, do đó nó không được đánh giá là quá mạnh.



Vì terminal nhẹ hơn nên chúng ta sẽ sử dụng dòng lệnh để khám phá cấu hình hệ thống.



Khi bạn khởi động, bạn sẽ thấy một màn hình màu cầu vồng ngắn, tiếp theo là thông báo chào mừng từ Raspberry và ở góc dưới bên trái là các thông báo hạt nhân liên quan đến quá trình khởi động.



Khi màn hình nền PI OS xuất hiện, hãy mở terminal và nhập:



```bash
uname -a
```


Lệnh này sẽ hiển thị phiên bản kernel hiện đang được sử dụng trên màn hình cùng với các thông tin khác.



![img](assets/it/26.webp)



Bạn cũng có thể xem thông tin về CPU và phần cứng bằng cách nhập:



```bash
lscpu
```



![img](assets/it/27.webp)



Và cũng xem `proc/mem/info`.



![img](assets/it/28.webp)



Để tìm hiểu phiên bản Debian và tên mã phát hành:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Sử dụng


Mặc dù hiệu suất có vẻ hạn chế (trên lý thuyết và so với sức mạnh của các máy móc hiện nay) nhưng PI Zero có hiệu suất cao, đặc biệt là khi dùng làm thiết bị đầu cuối.





- Trước tiên, bạn có thể vào menu chính và tìm hiểu thêm từ bảng _Thêm/Xóa phần mềm_, nơi bạn sẽ tìm thấy một số tiện ích để lập trình và thực hành. Lưu ý rằng bạn cũng có thể thực hiện việc này từ terminal, nhưng luôn phải có quyền `root`.



![img](assets/it/33.webp)





- Bạn có thể "sử dụng" thiết bị ngoại tuyến này để lưu trữ nhiều loại tài liệu mật, có thể truy cập khi cần mà không cần phải kết nối với Internet.
- Bạn có thể sử dụng cấu hình này để generate khóa GPG của mình một cách an toàn.
- Bạn thậm chí có thể tận dụng "đồ chơi" mới này như một thiết bị ký airgap, [theo lời khuyên của Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Trong số các ví mà tôi quen thuộc, ví duy nhất cung cấp bản phát hành 32-bit là Electrum. Vâng: Zero IP như chúng tôi đã chuẩn bị trong hướng dẫn này sẽ cho phép bạn giữ khóa riêng ngoại tuyến khi thiết lập Wallet airgap mà chúng tôi đã đề cập trong hướng dẫn này:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Kết luận


Thiết lập này có lẽ có một điểm yếu lớn: thẻ nhớ micro SD là một phương tiện có thể gây ra sự cố. Nó dễ bị hỏng khi sử dụng nhiều; có lẽ bạn đã có kinh nghiệm với điều này, từ việc sử dụng nó trên điện thoại. Sau khi cài đặt tất cả phần mềm bạn muốn sử dụng trên Zero airgap IP, hãy sao lưu cẩn thận thẻ nhớ micro SD quý giá của bạn bằng công cụ Raspi OS có sẵn.



![img](assets/it/34.webp)



Khi nhu cầu của bạn tăng lên, cùng với khả năng tài chính, bạn có thể khám phá các giải pháp Raspberry khác hoặc các giải pháp tương tự. Ví dụ, nói về bộ nhớ, PI 5 cung cấp khả năng lắp ráp ổ đĩa M2 NVME, chắc chắn mạnh mẽ hơn microSD.



Đừng quên ghi chú và ghi lại từng bước cài đặt phần mềm tiện ích mà bạn sắp sử dụng ngoại tuyến. **sớm muộn gì một hệ điều hành Raspi được cập nhật cũng sẽ ra mắt** mà bạn chắc chắn sẽ muốn tận dụng. Lúc đó, bạn sẽ phải xóa mọi thứ và làm lại từ đầu (có lẽ với một thẻ nhớ micro SD mới 😂).



Bài tập chúng ta vừa thực hiện, giả sử đây cũng là lần đầu tiên bạn thử nghiệm, bạn sẽ nhớ rất lâu. Không phải lúc nào cũng có thể dành phần cứng cho các hoạt động `nhúng` ngoại tuyến mà không bỏ qua việc chú ý đến một máy tính được kết nối mạng để bật và kiểm tra định kỳ.



Nhưng bạn đã làm được rồi, xin chúc mừng! Và bạn sẽ có thể gợi ý giải pháp này cho tất cả những ai cần tiết kiệm ngân sách.